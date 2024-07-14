from src.utils import NamedClass
from collections import Counter

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
        "sensation": 0,
    """
    your_effects = {}
    their_effects = {}

    # Moving their limb, going airborn, etc
    extra_effects = ""

    # Fist smash knee, flat palm smack face, butt below hands, etc
    your_requirements = []
    # Prone, >2 rage, etc
    their_requirements = []


    # How many times does it appear in the deck?
    # TODO slightly different images?
    count = 1

    # A dict that holds all defined cards by:
    # string of class name -> type
    all_types = {}
    @classmethod
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        # Register each subclass in the all_cards dictionary
        # TODO SLOPPY
        if cls.__name__ != "Life":
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
        cost = sum(cls.your_effects.values())
        cost -= sum(cls.their_effects.values())

        req_costs = {
            "touch": -1,
            "smack": -2,
            "smash": -3,

            "anywhere": 1,
        }
        for k, v in req_costs.items():
            if k in ", ".join(cls.your_requirements):
                cost += v

        # TODO theirs
        return cost

    @classmethod
    def get_description(cls):
        """
        Return the html str of this cards description
        """
        # Simple helper function for +1/-1, etc
        def status_string(item):
            k, v = item
            if v == 0:
                return ""
            sign = "" if v < 0 else "+"
            return f"<span class='{k} status'>{sign}{v} {k}</span>"

        # TODO html param/func?
        your_string = ", ".join(
            status_string(i) for i in cls.your_effects.items())
        their_string = ", ".join(
            status_string(i) for i in cls.their_effects.items())

        s = ""
        if cls.your_requirements:
            s += f"If you {'and '.join(cls.your_requirements)}:\n"
        if cls.their_requirements:
            s += f"and they {'and '.join(cls.their_requirements)}:\n"
        if your_string:
            s += f"<hr>You get {your_string}\n"
        if their_string:
            s += f"<hr>They get {their_string}\n"

        # Emphasize the keywords that are important for the rules
        keywords = [
            "smash", "smack",
            "flat palm", "fist", "grasp hand",
        ]

        for keyword in keywords:
            s = s.replace(keyword, f"<b class='{keyword}'>{keyword}</b>")

        return s

    @classmethod
    def sorted_types(cls):
        return sorted(cls.all_types.values(), key=lambda c: c.name)

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
Below, all card types are defined:
"""
# Strikes (hit them to hurt them)
class BloodyNose(Card):
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

class CheekSlap(Card):
    your_requirements = [
        "smack a flat palm into their face"
    ]
    their_effects = {
        "dignity": +1,
        "rage": -1,
        "pain tolerance": -2,
    }

class FrontJab(Card):
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

# Psych-outs
class TapOut(Card):
    your_requirements = [
        "touch a flat palm to them anywhere"
    ]
    your_effects = {
        "dignity": -1,
    }
    their_effects = {
        "rage": -1,
    }

# Poses (stance to help yourself)

# Control (grab them to move them)

# Movement


# Card ideas:
"""
Cheek Slap  Flat pam smack face      +1 dignity -2 pain tolerance, -1 rage
Jab Fist smack head/torso       -1 focus    -2 pain tolerance, -1 stamina
Tap Out Both flat palms touch them anywhere
False Surrender Flat palms raised above your head       -2 dignity  -2 rage,
Feint
Thumb-eye Press Both grasp hands touch face     -1 dignity

Limb Control
Control Wrist   Grasp hand touches their wrist      -1 focus, -1 stamina    You can move that limb anywhere
Slap Away   Flat palm smack their limb          You can move that limb anywhere
Power Grip  Both grasp hands touch their wrist


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
