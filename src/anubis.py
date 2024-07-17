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
        "Rule": 3,
        "Loss": 8,
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

        # Final totals from the other categories
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

        draw_chances = {cat: draw_chance(cat) for cat in cat_totals}
        # Put totals into dict to see them
        cat_totals["Deck"] = deck_total
        cls.category_sizes["Deck"] = deck_desired

        need_more = {
            k: cls.category_sizes[k] - v
            for k, v in cat_totals.items()
        }

        return (
            f"Final balance: {status_string(cat_totals)}\n"
            f"Desired totals: {status_string(cls.category_sizes)}\n"
            f"Need more: {status_string(need_more)}\n"
            f"Draw Chance: {status_string(draw_chances)}\n"
        )

    @classmethod
    def status_totals(cls):
        """
        Return a str report of how many of each status is added to
        or taken away
        """
        cards = Card.all_types.values()
        statuses = cls.desired_status_totals.keys()

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
            k: cls.desired_status_totals[k] - all_totals[k]
            for k in statuses
        }


        final_results = [
            ("Plusses on you", f"{status_string(your_plus)}\n"),
            ("Minuses on you", f"{status_string(your_minus)}\n"),
            ("Plusses on them", f"{status_string(their_plus)}\n"),
            ("Minuses on them", f"{status_string(their_minus)}\n"),
            ("<hr>", ""),
            ("Sum on you", f"{status_string(your_totals)}\n"),
            ("Sum on them", f"{status_string(their_totals)}\n"),
            ("<hr>", ""),
            ("All Plusses", f"{status_string(plus_totals)}\n"),
            ("All minuses", f"{status_string(minus_totals)}\n"),
            ("<hr>", ""),
            ("Final balance", f"{status_string(all_totals)}\n"),
            ("Desired totals", f"{status_string(cls.desired_status_totals)}\n"),
            ("Need more", f"{status_string(need_more)}\n"),
        ]

        return "".join(
            f"<div style='break-inside: avoid;'>{k}{v}</div>"
            for k, v in final_results
        )
