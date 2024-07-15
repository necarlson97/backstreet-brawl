from src.utils import status_string
from src.card import Card

class Anubis():
    """
    As anubis balances our heart against a feather, this class balances
    the full deck against a desired set of traits to see if we need to add more
    cards
    """


    # How long we'd like the game to run
    desired_rounds = 6
    # How many cards in the player's hand at a time
    draw_size = 9

    # How many we want of each category
    category_sizes = {
        "Strike": 20,
        "Grapple": 10,
        "Pose": 10,
        "Psych Out": 10,
        "Reaction": 10,
        "Control": 5,
        "Movement": 5,
        "Upkeep": 3,
    }

    """
    I think we want the physical cards all negative
    by a certain amount, the psych cards pretty even,
    and stamina and focus to be balanced by breathing card
    mult by number of turns. So something like:

    -3r oxygen
    -3r blood
    -3r pain tolerance
    -3r senses
    0 dignity
    0 rage
    -1.5r focus (get 1-2 focus per turn)
    -2r stamina (get 2ish stamina per turn)
    """
    desired_status_totals = {
        "oxygen": -3 * desired_rounds,
        "blood": -3 * desired_rounds,
        "pain tolerance": -3 * desired_rounds,
        "senses": -3 * desired_rounds,

        "rage": 0,
        "dignity": 0,
        "focus": int(-1.5 * desired_rounds),
        "stamina": -2 * desired_rounds,
    }

    @classmethod
    def category_totals(cls):
        cat_totals = {}
        for card in Card.sorted_types():
            cat = card.get_category()
            cat_totals[cat] = cat_totals.get(cat, 0) + 1

        deck_total = len(Card.sorted_types())
        deck_desired = sum(v for v in cls.category_sizes.values())

        def draw_chance(cat):
            # How likely are we to get one at the start of a game
            # (not exactly correct)
            ratio = (cat_totals[cat] / deck_total) * cls.draw_size
            desired_ratio = (
                (cls.category_sizes[cat] / deck_desired) * cls.draw_size)
            percent = round(100 * ratio)
            desired_persent = round(100 * desired_ratio)
            return f"{percent}% ({desired_persent}%)"

        s = ""
        for cat, total in cat_totals.items():
            desired = cls.category_sizes[cat]
            dc = draw_chance(cat)
            s += f"{cat}: {total-desired} ({total}/{desired}) {dc}\n"

        # Total deck size
        s += (
            f"For a final deck size of "
            f"{deck_total-deck_desired} ({deck_total}/{deck_desired})"
        )
        return s

    @classmethod
    def status_totals(cls):
        """
        Return a str report of how many of each status is added to
        or taken away
        """
        cards = Card.all_types.values()
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

        need_more = {
            k: cls.desired_status_totals[k] - v
            for k, v in all_totals.items()
        }

        # TODO pretty print dicts
        return (
            f"Plusses on you: {status_string(your_plus)}\n"
            f"Minuses on you: {status_string(your_minus)}\n"
            f"Plusses on them: {status_string(their_plus)}\n"
            f"Minuses on them: {status_string(their_minus)}\n"

            "\n"
            f"Sum on you: {status_string(your_totals)}\n"
            f"Sum on them: {status_string(their_totals)}\n"
            "\n"
            f"All Plusses: {status_string(plus_totals)}\n"
            f"All minuses: {status_string(minus_totals)}\n"
            "\n"
            f"Final balance: {status_string(all_totals)}\n"
            f"Desired totals: {status_string(cls.desired_status_totals)}\n"
            f"Need more: {status_string(need_more)}\n"
        )
