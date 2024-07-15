from abc import ABC
from dataclasses import dataclass

from src.utils import NamedClass, status_string, get_cost_from_menu

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
                f"<i class='reminder'>{self.desc}</i> {status_effects}"
            )

    @dataclass
    class Status:
        level: int
        state: str
    stances = {
        "standing": Stance(
            name='standing', rarity=1, stamina=2, focus=2,
            desc="feet flat on ground, hips aligned between the feet, hips above knee-level"),
        "crouching": Stance(
            name='crouching', rarity=1, stamina=1, focus=2,
            desc="feet on ground, hips aligned between the feet, hips above knee-level"),
        "sitting": Stance(
            name='sitting', rarity=2, stamina=2, focus=1,
            desc="hips below knee-level, chest above knee-level"),
        "prone": Stance(
            name='prone', rarity=2, stamina=3, focus=0,
            desc="hips and chest below knee-level"),
        "off balance": Stance(
            name='off balance', rarity=1, stamina=0, focus=0,
            desc="at least one limb on the ground"),
        "airborne": Stance(
            name='airborne', rarity=2, stamina=2, focus=0,
            desc="nothing touching ground"),
    }

    # Parts of a requirement, and how much these keywords effect cost
    strike_types = {
        "place": -.5,
        "touch": -1,
        "smack": -2,
        "smash": -3,
        "sandwich": -3,
    }

    # Targets, and how easy to hit they are
    strike_targets = {
        "anywhere": 1,
        "forearm": 0,
        "calf": 0,
        "foot": 0,
        # "hand": 0, TODO fucked by grasp hand. Can we call it something else?
        "head": -0.5,
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
            "move that limb": 3,
            "move your hips": 2,
            "keep this": 1,
        }
        add_to_cost(dikt, extra_costs, cls.extra_effects)

        for r in cls.your_requirements:
            add_to_cost(dikt, cls.strike_types, r, key_add="your strike type")
            add_to_cost(dikt, cls.strike_targets, r, key_add="your target")
            add_to_cost(
                dikt, {k: -v.rarity for k, v in cls.stances.items()},
                r, key_add="your stance")

        for r in cls.their_requirements:
            add_to_cost(
                dikt, {k: 3 + v for k, v in cls.strike_types.items()},
                r, key_add="their strike type")
            add_to_cost(
                dikt, {k: -v.rarity for k, v in cls.stances.items()},
                r, key_add="their stance")

        if issubclass(cls, Reaction):
            dikt["reaction"] = 1

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

        reqs = ""
        if cls.your_requirements:
            yr = "\nand ".join(cls.your_requirements)
            reqs += f"If you {yr}"
        if cls.their_requirements:
            tr = "\nand ".join(cls.their_requirements)
            reqs += f"\nwhile they {tr}"
        if cls.your_requirements or cls.their_requirements:
            reqs += ":\n"

        statements = [r for r in [reqs] if r]
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
            | cls.strike_types.keys() | cls.stances.keys()
        )
        for keyword in keywords:
            s = s.replace(keyword, f"<b class='{keyword}'>{keyword}</b>")

        return s

    @classmethod
    def get_category(cls):
        return ", ".join(c.human_name() for c in cls.__bases__)

    @classmethod
    def is_rule(cls):
        return Rule in cls.__bases__

    @classmethod
    def sorted_types(cls):
        cat_order = [
            "Strike", "Grapple", "Psych Out", "Control",
            "Pose", "Movement", "Reaction", "Rule"
        ]
        return sorted(
            cls.all_types.values(),
            key=lambda c: (cat_order.index(c.get_category()), c.name)
        )

    @classmethod
    def reprints(cls):
        return {
        }

"""
Below, all card types are defined in separate categories, based loosely
on what they are 'trying to do'
"""
class Strike(Card, ABC):
    # hit them to hurt them
    # TODO want to have a good mix of punches/kicks
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
        "senses": +1,
        "rage": -2,
        "pain tolerance": -1,
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
# Kicks
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
        "pain tolerance": -1,
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
        "rage": +2,
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
    # Want a good mix of blood/+rage (bite, scratch)
    # and oxygen/-rage (presses, squeezes)
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
class RakeArms(Grapple):
    your_requirements = [
        "touch both grasp hands to their forearm or bicep"
    ]
    your_effects = {
        "stamina": -1,
    }
    their_effects = {
        "blood": -2,
        "stamina": -1,
        "rage": +1,
    }
class DesperateBite(Grapple):
    your_requirements = [
        "touch your head to them anywhere"
    ]
    your_effects = {
        "focus": -2,
    }
    their_effects = {
        "blood": -2,
        "pain tolerance": -2,
        "rage": +1,
    }
class GnawFace(Grapple):
    your_requirements = [
        "touch your head to their head"
    ]
    your_effects = {
        "focus": -1,
        "dignity": -1,
    }
    their_effects = {
        "blood": -1,
        "pain tolerance": -1,
        "senses": -2
    }
# Chokes/presses
class NakedPress(Grapple):
    your_requirements = [
        "sandwich their neck between your forearm and torso",
    ]
    your_effects = {
        "focus": -1,
        "dignity": +1,
    }
    their_effects = {
        "oxygen": -2,
        "senses": -1
    }
class ThumbStrangle(Grapple):
    your_requirements = [
        "touch both grasp hands to their neck",
    ]
    your_effects = {
        "dignity": -1,
    }
    their_effects = {
        "oxygen": -2,
        "senses": -1,
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
    their_effects = {
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
class LowSprawl(Pose):
    your_requirements = [
        "are prone",
        "fully extend two or more limbs",
    ]
    your_effects = {
        "focus": +1,
        "oxygen": +1,
    }
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
class Mabu(Pose):
    your_requirements = [
        "are crouching, with feet parallel",
        "have both hands below waist-height",
    ]
    your_effects = {
        "focus": +1,
        "dignity": +1,
        "rage": -1,
    }
class GulpAir(Pose):
    your_requirements = [
        "are standing or crouching",
        "touch both hands to your knees",
    ]
    your_effects = {
        "focus": +1,
        "oxygen": +2,
        "dignity": -1,
    }
class CrossGaurd(Pose):
    your_requirements = [
        "place both forearms between your chest and theirs",
    ]
    your_effects = {
        "oxygen": +1,
        "dignity": +1,
        "rage": -1,
    }
class Vasoconstrict(Pose):
    your_requirements = [
        "prone",
        "at least one limb fully extended"
    ]
    your_effects = {
        "blood": +2,
        "rage": -1,
        "focus": +1
    }
class FetalCurl(Pose):
    your_requirements = [
        "prone",
        "at least two feet or hands touching torso or head"
    ]
    your_effects = {
        "blood": +1,
        "stamina": +1,
        "focus": +1,
    }

class Control(Card, ABC):
    # grab them to move them
    pass
class SqueezeWrist(Control):
    your_requirements = [
        "touch a grasp hand to their hand or forearm"
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
class TuckJump():
    your_requirements = [
        "lift both feet above knee-level"
    ]
    your_effects = {
        "stamina": -1,
    }
    extra_effects = (
    )
class HighJump():
    your_requirements = [
        "crouching"
    ]
    your_effects = {
        "stamina": -1,
    }
    extra_effects = (
        "Move your hips a limb-length in any direction"
    )

class Reaction(Card, ABC):
    # Card played on their turn
    # TODO is this a good idea?
    pass
class CatchPunch(Reaction):
    your_requirements = [
        "can have a grasp hand to touch their fist in one motion"
    ]
    their_requirements = [
        "are smacking/smashing you with a fist"
    ]
    your_effects = {
        "focus": -1,
        "stamina": -1,
    }
    extra_effects = (
        "Negate their card's effects on you"
    )
class UkeBlock(Reaction):
    your_requirements = [
        "can have your forearm touch their hand in one motion"
    ]
    their_requirements = [
        "are smacking/smashing you with a hand"
    ]
    your_effects = {
        "focus": -1,
        "pain tolerance": -1,
    }
    extra_effects = (
        "Negate their card's effects on you"
    )
class FirmRepost(Reaction):
    your_requirements = [
        "can smash your fist into their torso in one motion",
    ]
    their_requirements = [
        "are smacking/smashing you"
    ]
    your_effects = {
        "focus": -1,
    }
    their_effects = {
        "oxygen": -1,
        "pain tolerance": -1,
        "focus": -1,
    }
class RetreatingShrimp(Reaction):
    your_requirements = [
        "prone"
    ]
    their_requirements = [
        "are grappling you"
    ]
    your_effects = {
        "stamina": -1,
    }
    extra_effects = (
        "Move your hips a limb-length away"
    )
class ChinUp(Reaction):
    their_requirements = [
        "are touch/smack/smashing you"
    ]
    your_effects = {
        "stamina": -1,
        "dignity": +1,
    }
    their_effects = {
        "rage": +1
    }

class Rule(Card, ABC):
    pass
class MoveLimb(Rule):
    your_effects = {
        "stamina": -1,
    }
    extra_effects = (
        "Move one of your limbs any way you like\n"
        "<i class='reminder'>A limb includes many joints, e.g.: "
        "wrist+elbow+shoulder. The head+torso+hips is also a limb.</i>"
        "<hr>"
        "Keep this card in your hand always\n"
        "You can play it multiple times a turn"
    )
class SwitchGrip(Rule):
    your_effects = {
        "stamina": -1,
    }
    extra_effects = (
        "Change out one or both hands<hr>"
        "Keep this card in your hand always\n"
        "You can play it multiple times a turn"
    )
class KeepBreathing(Rule):
    extra_effects = (
        "At the start of your turn,\n"
        "gain focus and stamina from your state:<hr>"
    ) + "<hr>".join(s.get_description() for s in Card.stances.values())
class ZZTest(Rule):
    your_requirements = [
        "smash a foot into their neck"
    ]

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
