from abc import ABC
from dataclasses import dataclass
import re
import random

from src.utils import (
    NamedClass, status_string, get_cost_from_menu,
    status_requirement, status_order, replace_status_requirement
)

import logging
logger = logging.getLogger("cards")

class Card(NamedClass):
    """
    Abstract class, that each specific type of card will sub-class
    Then each instance of a subclass is the individual card,
    """
    flavor_text = "todo flavor"

    # What +/- effects it has on the 8 statuses:
    """
        "focus": 0,
        "rage": 0,
        "dignity": 0,
        "stamina": 0,

        "oxygen": 0,
        "blood": 0,
        "pain tolerance": 0,
        "senses": 0,
    """
    # TODO senses vs sensation
    your_effects = {}
    their_effects = {}

    # Moving their limb, going airborn, etc
    extra_effects = ""

    # Fist smash knee, flat palm smack face, butt below hands, etc
    your_requirements = []
    # Prone, >=2 rage, etc
    their_requirements = []

    # The different states the body can be in, and how much stamina each state
    # recovers per turn
    @dataclass
    class Stance:
        name: str
        desc: str
        rarity: int
        focus: int
        stamina: int

        def get_description(self):
            status_effects = status_string({
                "stamina": self.stamina, "focus": self.focus
            }, remove_zero=True)
            return (
                f"{self.name}: "
                f"<i class='reminder'>{self.desc}</i> "
                f"<div>{status_effects}</div>"
            )

    @dataclass
    class Status:
        level: int
        state: str
    stances = {
        "standing": Stance(
            name='standing', rarity=1, stamina=2, focus=2,
            desc="feet flat on ground, hips aligned between the feet, "
                 "hips above knee‑level"),
        "crouching": Stance(
            name='crouching', rarity=1, stamina=1, focus=2,
            desc="feet on ground, hips aligned between the feet, "
                 "hips above knee‑level"),
        "sitting": Stance(
            name='sitting', rarity=2, stamina=2, focus=1,
            desc="hips below knee‑level, chest above knee‑level"),
        "prone": Stance(
            name='prone', rarity=2, stamina=3, focus=0,
            desc="hips and chest below knee‑level"),
        "off balance": Stance(
            name='off balance', rarity=1, stamina=2, focus=-1,
            desc="at least one limb on the ground"),
        "airborne": Stance(
            name='airborne', rarity=2, stamina=2, focus=0,
            desc="nothing on the ground"),
    }

    # Parts of a requirement, and how much these keywords effect cost
    strike_types = {
        "place": -.5,
        "touch": -1,
        "smack": -2,
        "smash": -3,
        "sandwich": -3,
        "wrap": -3,

        "posing": -1,
        "psyching": -1,
    }

    # Targets, and how easy to hit they are
    strike_targets = {
        "anywhere": 1,
        "forearm": 0,
        "calf": 0,
        "foot": 0,
        "hand": 0,
        "head": -0.5,
        "torso": 0,
        "chest": -0.5,
        "hip": -0.5,
        "groin": -1,
        "bicep": 0,
        "thigh": 0,
        "neck": -1,
        "face": -0.5,
    }

    # The switchable magnetic hands names
    # TODO okay to put foot here?
    hands = {"fist", "flat palm", "grasp hand"}

    # How many times does it appear in the deck?
    # TODO slightly different images?
    count = 1

    # Different heights, with a human-readable name and a cm value
    # TODO does this make sense?
    heights = {
        "knee": 5,
        "waist": 10,
        "chest": 14,
        "eye": 18,
    }

    # A dict that holds all defined cards by:
    # string of class name -> type
    all_types = {}
    @classmethod
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        # Register each subclass in the all_cards dictionary
        # TODO SLOPPY
        if ABC not in cls.__bases__:
            cls.all_types[cls.__name__] = cls
            cls.index = len(cls.all_types)

            # TODO SLOPPY
            for existing in cls.all_types.values():
                matching_text = cls != existing and cls.flavor_text == existing.flavor_text
                not_todo = "todo" not in cls.flavor_text.lower()
                if cls.flavor_text and matching_text and not_todo:
                    raise ValueError(
                        f"Duplicate flavor: "
                        f"{existing.name} ({existing.flavor_text}) vs "
                        f"{cls.name} ({cls.flavor_text})"
                    )

    def __str__(self):
        return f"{self.name}"

    @classmethod
    def get_cost(cls):
        """
        Return the 'cost' for this card - should ideally be
        0 for all cards, as in their negatives balance their positives.

        Easy to execute (touch) = 2 points to spend
        Hard to execute (smash) = 3 points to spend
        (Then if it costs 1-, that's another point to spend)
        Moving limb = 3pts
        Jumping = 2pts

        "Touch = move that makes contact, from any distance away
        Smack = move that makes contact from > a forearms length away
        Smash = Move that makes contact from > a full limbs length away"
        "Focus, Rage, Dignity, Stamina
        Oxygen, Blood, Pain Tolerance, Senses
        """
        return sum(v for v in cls.get_cost_components().values())

    @classmethod
    def get_cost_components(cls):
        """
        Return a dict of the each component that goes into calculating the cost
        """
        # TODO could clean by moving to cost calc class
        dikt = {}

        for k, v in cls.your_effects.items():
            dikt[f"you get {k} {v}"] = v
        for k, v in cls.their_effects.items():
            dikt[f"they get {k} {v}"] = -v

        def add_to_cost(dikt, menu, source, key_add=""):
            # Check some piece of source text (requirements, effects, w/e)
            # and see if it changes our cost
            dikt.update({
                f"{key_add} {k}": v
                for k, v in get_cost_from_menu(menu, source).items()
            })
            return dikt

        extra_costs = {
            "Negate their card": 2,
            "move the limb": 2,
            "move that limb": 3,
            "move your hips": 2,
            "move their hips": 3,
            "to a prone": 2,
            "keep this": 1,
            "rotate your": 2,
        }
        add_to_cost(dikt, extra_costs, cls.extra_effects)
        # If extra costs has a requirement...
        # TODO just considers stance, should break out entire req check into
        # separate function, than call here.
        if all(s in cls.extra_effects.lower() for s in [',', 'if ']):
            try:
                extra_req, _ = cls.extra_effects.lower().split(',')
                add_to_cost(
                    dikt, {k: -v.rarity for k, v in cls.stances.items()},
                    extra_req, key_add="extra req"
                )
            except ValueError:
                print(f"Couldn't split {cls.extra_effects.lower()}")

        def check_status_cost(r, person="you"):
            # Helper for adding/subtracting cost for my/their status costs
            # (Note that we don't split on OR, so just, like,
            # put the one you want to count to score as the 1st one)
            for ret in [status_requirement(s) for s in r.split("and")]:
                if not ret:
                    continue
                status, gtlt, value = ret
                # Should lower costs if it is 'hard' e.g, >=5
                cost = (-value + 1) / 2
                # If it is <= then lower is harder
                if "<=" in gtlt:
                    cost = -4 + ((value + 1) / 2)
                dikt[f"{person} need {gtlt}{value} {status}"] = cost

        other_requrements = {
            "not touching": -0.5,
            "was moved": -1,
            "-level": -0.5,
        }
        for r in cls.your_requirements:
            check_status_cost(r)

            add_to_cost(
                dikt, cls.strike_types, r, key_add="your strike type")

            add_to_cost(dikt, other_requrements, r)

            target = r
            split_words = ["to their", "to them", "to that", "to your"]
            for sw in split_words:
                try:
                    weapon, target = target.split(sw)
                    break
                except ValueError:
                    weapon, target = ("", target)

            add_to_cost(
                dikt, cls.strike_targets, target, key_add="your target")
            add_to_cost(
                dikt, {k: -v.rarity for k, v in cls.stances.items()},
                r, key_add="your stance")

            # TODO could price out weapons as inverse of target cost,
            # but eh all would likely be 0
            weapons = weapon.replace(" or ", ", ").split(", ")
            if len(weapons) > 3:
                dikt[f"many weapons: {weapons}"] = 0.5

        from src.all_cards import Reaction
        if issubclass(cls, Reaction):
            dikt["reaction"] = 0.5

        for r in cls.their_requirements:
            check_status_cost(r, "they")

            # If we are negating, it is better to negate worse
            if issubclass(cls, Reaction):
                if "Negate" in cls.extra_effects:
                    add_to_cost(
                        dikt, {k: 3 + v for k, v in cls.strike_types.items()},
                        r, key_add="negate their strike type")
                # If we are just reacting, it is better to react to more common
                else:
                    add_to_cost(
                        dikt, {k: v for k, v in cls.strike_types.items()},
                        r, key_add="activate on their strike type")

            add_to_cost(
                dikt, {k: -v.rarity for k, v in cls.stances.items()},
                r, key_add="their stance")

        return dikt

    @classmethod
    def get_cost_breakdown(cls):
        """
        Html hover title of why it costs X
        """
        s = "\n".join(
            f"{k}: {v}" for k, v in cls.get_cost_components().items()
        )
        s += f"\n\ntotal: {cls.get_cost()}"
        return s

    @classmethod
    def get_description(cls):
        """
        Return the html str of this cards description
        """
        parsed_your_reqs = [
            replace_status_requirement(r) for r in cls.your_requirements
        ]
        parsed_their_reqs = [
            replace_status_requirement(r) for r in cls.their_requirements
        ]

        reqs = ""
        if cls.your_requirements:
            yr = "\nand ".join(parsed_your_reqs)
            reqs += f"If you {yr}"
        if cls.their_requirements:
            tr = "\nand ".join(parsed_their_reqs)
            reqs += f"\nwhile they {tr}"
        if cls.your_requirements or cls.their_requirements:
            reqs += ":\n"
        statements = [r for r in [reqs] if r]

        def sort_statuses(dikt):
            # Order by:
            # positives first, then by status order
            s_dikt = sorted(
                dikt.items(),
                key=lambda item: (item[1] <= 0, status_order.index(item[0]))
            )
            return { k: v for k, v in s_dikt}
        ye = sort_statuses(cls.your_effects)
        te = sort_statuses(cls.their_effects)
        your_string = ", ".join(
            status_string(i) for i in ye.items())
        their_string = ", ".join(
            status_string(i) for i in te.items())


        if your_string:
            statements.append(
                f"You get {your_string}\n")
        if their_string:
            statements.append(
                f"They get {their_string}\n")
        if cls.extra_effects:
            statements.append(
                f"{cls.extra_effects}\n")

        s = "<hr>".join(statements)

        # Emphasize the keywords that are important for the rules
        # TODO any extras?
        from src.loss_cards import Loss
        if not issubclass(cls, Loss):
            keywords = (
                set() | cls.hands
                | cls.strike_types.keys() | cls.stances.keys()
            )
            for keyword in keywords:
                s = s.replace(keyword, f"<b class='{keyword}'>{keyword}</b>")

        # For now, consider all hypens as 'non breaking',
        # so replace them with non-break unicode variant
        s = s.replace('-', '‑')

        return s.strip()

    @classmethod
    def get_category(cls):
        return ", ".join(c.human_name() for c in cls.__bases__)

    @classmethod
    def is_rule(cls):
        from src.all_cards import Rule
        return Rule in cls.__bases__

    @classmethod
    def sorted_types(cls):
        cat_order = [
            "Strike", "Grapple", "Psych Out", "Control",
            "Pose", "Movement", "Reaction", "Rule", "Loss"
        ]
        return sorted(
            cls.all_types.values(),
            key=lambda c: (cat_order.index(c.get_category()), c.name)
        )

    @classmethod
    def real_cards(cls):
        return [
            ct for ct in cls.all_types.values()
            if ct.is_real()
        ]
    @classmethod
    def is_real(cls):
        return cls.get_category() not in ["Rule", "Loss"]

    @classmethod
    def get_hand(cls):
        from src.anubis import Anubis
        return [
            random.choice(cls.real_cards())
            for i in range(Anubis.draw_size)
        ]

    @classmethod
    def reprints(cls):
        """
        If you just need to print a few more, you can list there
        names here
        """
        from src.all_cards import (
            TuckJump, ContactRules, FightIgnition, YourTurn, KeepBreathing,
            LegLock,
        )
        return {
        }
