from src.utils import NamedClass, status_string
from collections import Counter
from abc import ABC, abstractmethod

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
    # Prone, >2 rage, etc
    their_requirements = []

    # The different states the body can be in, and how much stamina each state
    # recovers per turn
    # TODO description for each
    state_stamina = {
        "standing": 1,
        "crouching": 2,
        "sitting": 2,
        "off balance": 1,
        "prone": 3,
        "airborne": 2,
    }
    state_focus = {
        "standing": 2,
        "crouching": 1,
        "sitting": 1,
        "off balance": 0,
        "prone": 0,
        "airborne": 0,
    }

    # Parts of a requirement, and how much these keywords effect cost
    strike_types = {
        "touch": -1,
        "smack": -2,
        "smash": -3,
    }

    # Targets, and how easy to hit they are
    strike_targets = {
        "anywhere": 1,
        "forearm": 0,
        "calf": 0,
        "foot": 0,
        "hand": 0,
        "head": 0,
        "torso": 0,
        "hips": 0,
        "bicep": 0,
        "thigh": 0,
        "neck": -1,
    }

    # The switchable magnetic hands names
    # TODO okay to put foot here?
    hands = {"fist", "flat palm", "grasp hand", "foot"}

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
        dikt = {}

        for k, v in cls.your_effects.items():
            dikt[f"you get {k} {v}"] = v
        for k, v in cls.their_effects.items():
            dikt[f"they get {k} {v}"] = -v

        def add_to_cost(dikt, menu, source):
            # Check some piece of source text (requirements, effects, w/e)
            # and see if it changes our cost

            # TODO find the min/max and add that? Rather than sum?
            for k, v in menu.items():
                if k.lower() in source.lower():
                    dikt[f"{k} ({source})"] = v
            return dikt

        extra_costs = {
            "Negate their card": 2,
            "move that limb": 3,
            "keep this": 1,
        }
        add_to_cost(dikt, extra_costs, cls.extra_effects)

        your_req_costs = {
            **cls.strike_types,
            **cls.strike_targets,
            # TODO should probs have a separate state-difficulty
            **{k: -v for k, v in cls.state_focus.items()},
        }

        if issubclass(cls, Reaction):
            dikt["Reaction"] = 1
        else:
            for r in cls.your_requirements:
                add_to_cost(dikt, your_req_costs, r)

        their_req_costs = {
            k: -3 + v for k, v in cls.state_focus.items()
        }
        for r in cls.their_requirements:
            add_to_cost(dikt, their_req_costs, r)
        return dikt

    @classmethod
    def get_cost_breakdown(cls):
        """
        Html hover title of why it costs X
        """
        return "\n".join(
            f"{k}: {v}" for k, v in cls.get_cost_components().items())

    @classmethod
    def get_description(cls):
        """
        Return the html str of this cards description
        """

        # TODO html param/func?
        your_string = ", ".join(
            status_string(i) for i in cls.your_effects.items())
        their_string = ", ".join(
            status_string(i) for i in cls.their_effects.items())

        statements = []
        if cls.your_requirements:
            statements.append(
                f"If you {'and '.join(cls.your_requirements)}:\n")
        if cls.their_requirements:
            statements.append(
                f"while they {'and '.join(cls.their_requirements)}:\n")
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
        keywords = (
            set() | cls.hands
            | cls.strike_types.keys() | cls.state_stamina.keys()
        )
        for keyword in keywords:
            s = s.replace(keyword, f"<b class='{keyword}'>{keyword}</b>")

        return s

    @classmethod
    def get_category(cls):
        return ", ".join(c.human_name() for c in cls.__bases__)

    @classmethod
    def is_upkeep(cls):
        return Upkeep in cls.__bases__

    @classmethod
    def sorted_types(cls):
        return sorted(
            cls.all_types.values(), key=lambda c: (c.get_category(), c.name))

    @classmethod
    def reprints(cls):
        return {
        }

    # TODO functions that will check cards to see:
    """
    * are they balanced
    * what stat is easiest/hardest to lower
    * what stats do many cards use
    * what status do few cards use
    """

    @classmethod
    def status_totals(cls):
        """
        Return a str report of how many of each status is added to
        or taken away
        """
        cards = cls.all_types.values()
        statuses = set(
            k for c in cards for k in
            list(c.your_effects.keys()) + list(c.their_effects.keys())
        )
        statuses = sorted(list(statuses))

        your_plus = {
            status: sum(
                card.your_effects[status]
                for card in cards
                if card.your_effects.get(status, 0) > 0
            )
            for status in statuses
        }
        your_minus = {
            status: sum(
                card.your_effects[status]
                for card in cards
                if card.your_effects.get(status, 0) < 0
            )
            for status in statuses
        }
        their_plus = {
            status: sum(
                card.their_effects[status]
                for card in cards
                if card.their_effects.get(status, 0) > 0
            )
            for status in statuses
        }
        their_minus = {
            status: sum(
                card.their_effects[status]
                for card in cards
                if card.their_effects.get(status, 0) < 0
            )
            for status in statuses
        }

        def sum_up(d1, d2):
            return {k: d1.get(k, 0) + d2.get(k, 0) for k in statuses}

        your_totals = sum_up(your_plus, your_minus)
        their_totals = sum_up(their_plus, their_minus)
        plus_totals = sum_up(your_plus, their_plus)
        minus_totals = sum_up(your_minus, their_minus)

        all_totals = sum_up(your_totals, their_totals)

        # Sanity check
        assert all_totals == sum_up(plus_totals, minus_totals)

        # TODO pretty print dicts
        return (
            f"Plusses on you: {your_plus}\n"
            f"Minuses on you: {your_minus}\n"
            f"Plusses on them: {their_plus}\n"
            f"Minuses on them: {their_minus}\n"

            "\n"
            f"Sum on you: {your_totals}\n"
            f"Sum on them: {their_totals}\n"
            "\n"
            f"All Plusses: {plus_totals}\n"
            f"All minuses: {minus_totals}\n"
            "\n"
            f"Final balance: {all_totals}\n"
        )

"""
Below, all card types are defined in separate categories, based loosely
on what they are 'trying to do'
"""
class Strike(Card, ABC):
    # hit them to hurt them
    pass
class BloodyNose(Strike):
    your_requirements = [
        "smash a fist into their face"
    ]
    your_effects = {
        "focus": -1,
        "rage": +1,
    }
    their_effects = {
        "blood": -1,
        "oxygen": -1,
        "pain tolerance": -1,
    }
class CheekSlap(Strike):
    your_requirements = [
        "smack a flat palm into their face"
    ]
    their_effects = {
        "dignity": +1,
        "rage": -1,
        "pain tolerance": -2,
    }
class FrontJab(Strike):
    your_requirements = [
        "smack a fist into them anywhere"
    ]
    your_effects = {
        "focus": -1,
    }
    their_effects = {
        "stamina": -1,
        "pain tolerance": -1,
    }
class Knifehand(Strike):
    your_requirements = [
        "smash a flat palm into their neck"
    ]
    your_effects = {
        "stamina": -1,
        "focus": +1,
    }
    their_effects = {
        "oxygen": -2,
        "focus": -1,
        "senses": -1,
    }
class Curbstomp(Strike):
    your_requirements = [
        "smack a foot into their head"
    ]
    their_requirements = [
        "are prone"
    ]
    your_effects = {
        "dignity": -1,
        "rage": +1,
    }
    their_effects = {
        "blood": -1,
        "senses": -2,
        "pain tolerance": -2,
    }
class GutKick(Strike):
    your_requirements = [
        "smack a foot into their torso"
    ]
    their_requirements = [
        "are sitting or prone"
    ]
    your_effects = {
        "dignity": -1,
        "rage": +1,
    }
    their_effects = {
        "oxygen": -2,
        "pain tolerance": -1,
    }
class Gastrizein(Strike):
    your_requirements = [
        "smack a foot into their torso"
    ]
    their_requirements = [
        "are standing"
    ]
    your_effects = {
        "dignity": +1,
    }
    their_effects = {
        "oxygen": -1,
        "pain tolerance": -1,
    }


class Grapple(Card, ABC):
    # closer, squeezing cards
    pass
class GougeEyes(Grapple):
    your_requirements = [
        "touch both grasp hands to their face"
    ]
    your_effects = {
        "dignity": -2,
    }
    their_effects = {
        "blood": -2,
        "senses": -2,
        "rage": +1,
    }

class PsychOut(Card, ABC):
    pass
class TapOut(PsychOut):
    your_requirements = [
        "touch a flat palm to them anywhere"
    ]
    your_effects = {
        "dignity": -1,
    }
    their_effects ={
        "rage": -1,
    }
class FauxWhiteFlag(PsychOut):
    your_requirements = [
        "lift both flat palms above your head"
    ]
    your_effects = {
        "dignity": -2,
        # "focus": +1,
    }
    their_effects = {
        "rage": -2,
    }
class Legerdemain(PsychOut):
    your_requirements = [
        "smack a grasp hand to them anywhere"
    ]
    your_effects = {
    }
    their_effects = {
        "focus": -1,
    }

class Pose(Card, ABC):
    # take a stance to help yourself
    pass
class Zenkutsu(Pose):
    your_requirements = [
        "are crouching, with one foot far forward and one far back",
        "have both hands between your waist-height and chest-height",
    ]
    your_effects = {
        "focus": -1,
        "senses": +1,
        "dignity": +1,
    }

class Control(Card, ABC):
    # grab them to move them
    pass
class SqueezeWrist(Control):
    your_requirements = [
        "touch a grasp hand to their hand/forearm"
    ]
    your_effects = {
        "focus": -1,
        "stamina": -1,
    }
    extra_effects = "You can move that limb any way you like"
class SlapAway(Control):
    your_requirements = [
        "smack a flat palm into their forearm"
    ]
    your_effects = {
        "focus": -1,
    }
    extra_effects = "You can move that limb any way you like"
class SweepLeg(Control):
    your_requirements = [
        "smash a foot into their calf"
    ]
    your_effects = {
        "stamina": -1,
    }
    their_effects = {
        "pain tolerance": -1
    }
    extra_effects = "You can move that limb any way you like"

class Movement(Card, ABC):
    # TODO better name?
    pass
class MoveLimb(Movement):
    your_effects = {
        "stamina": -1,
    }
    extra_effects = (
        "Move one of your limbs any way you like<hr>"
        "Keep this card in your hand always.\n"
        "You can play it multiple times a turn."
    )
class SwitchGrip(Movement):
    your_effects = {
        "stamina": -1,
    }
    extra_effects = (
        "Change out one or both hands<hr>"
        "Keep this card in your hand always.\n"
        "You can play it multiple times a turn."
    )
class TuckJump():
    your_requirements = [
        "lift both feet above knee-level"
    ]
    your_effects = {
        "stamina": -1,
    }
    extra_effects = (
        "Stay airborne at the start of next turn"
    )

class Reaction(Card, ABC):
    # Card played on their turn
    # TODO is this a good idea?
    pass
class CatchPunch(Reaction):
    your_requirements = [
        "play this when a card smacks/smashes you with a fist"
    ]
    your_effects = {
        "focus": -1,
        "stamina": -2,
    }
    extra_effects = "Negate their cards effects on you"

class Upkeep(Card, ABC):
    pass
class SteadyBreath(Upkeep):
    extra_effects = (
        "At the start if your turn, gain stamina depending on your state:<hr>"
    ) + "<hr>".join(
        f"{k}: " + ", ".join(filter(None, [
            status_string(("stamina", Card.state_stamina[k])),
            status_string(("focus", Card.state_focus[k])),
        ]))
        for k in Card.state_stamina
    )

# Card ideas:
"""
Feint
Thumb-eye Press Both grasp hands touch face     -1 dignity

Limb Control
Slap Away   Flat palm smack their limb          You can move that limb anywhere
Power Grip  Both grasp hands touch their wrist

Look over fighting moves, just add a bunch


Movement
Jump    Crouching       "-2 stamina
-1 rage
+1 dignity
For this turn, you can move"


Taunt - raise their rage. If high enough, they 'red out' and...
focus drops to 2?
...
"""

# Unused flavor text:
"""
...
"""
