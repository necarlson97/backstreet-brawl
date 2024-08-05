from src.utils import status_string, draw_chance
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
        "Strike": 25,
        "Grapple": 15,
        "Pose": 15,
        "Psych Out": 15,
        "Reaction": 15,
        "Control": 10,
        "Movement": 5,
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
        "stamina": int(-0.5 * desired_rounds),
    }

    @classmethod
    def category_totals(cls):
        cat_totals = {}
        for card in Card.sorted_types():
            cat = card.get_category()
            cat_totals[cat] = cat_totals.get(cat, 0) + 1

        not_real_cards = ["Rule", "Loss"]
        cat_totals = {
            k: v for k, v in cat_totals.items()
            if k not in not_real_cards
        }
        cat_desired = {
            k: v for k, v in cls.category_sizes.items()
            if k not in not_real_cards
        }

        # Final totals from the other categories
        deck_total = sum(v for v in cat_totals.values())
        deck_desired = sum(v for v in cat_desired.values())

        def draw_vs_desired_chance(cat):
            # How likely are we to get one at the start of a game
            # (not exactly correct)
            percent = draw_chance(
                cat_totals[cat], deck_total, cls.draw_size)
            desired_persent = draw_chance(
                cat_desired[cat], deck_desired, cls.draw_size)
            return f"{percent} ({desired_persent})"

        draw_chances = {
            cat: draw_vs_desired_chance(cat) for cat in cat_totals
        }
        # Put totals into dict to see them
        cat_totals["Deck"] = deck_total
        cls.category_sizes["Deck"] = deck_desired

        need_more = {
            k: cls.category_sizes[k] - v
            for k, v in cat_totals.items()
        }

        final_results = {
            "Need more": need_more,
            "Final balance": cat_totals,
            "Desired totals": cls.category_sizes,
            "Draw Chance": draw_chances,
        }
        return"".join(
            f"<div style='break-inside: avoid;'>{k}{status_string(v)}</div>"
            for k, v in final_results.items()
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

        # TODO by percent or something
        reccomendations = {
            "Need more": need_more,
            "Not enough minus on them":
                {k: v for k, v in their_minus.items() if v > 3*-cls.draw_size},
            "Not enough minus on you":
                {k: v for k, v in your_minus.items() if v > -cls.draw_size},
            "Too much plus on you":
                {k: v for k, v in your_plus.items() if v > 2*cls.draw_size},
            "Not enough pluses on you":
                {k: v for k, v in your_plus.items() if v < cls.draw_size},
            "Not enough pluses on them":
                {k: v for k, v in their_plus.items() if v < cls.draw_size},
        }


        detailed_results = [
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
        ]

        # TODO GROSS
        detailed_info = "".join(
            f"<div style='break-inside: avoid;'>{k}{v}</div>"
            for k, v in detailed_results
        )
        best_info = "".join(
            f"<div style='break-inside: avoid;'>{k}{status_string(v)}</div>"
            for k, v in reccomendations.items()
        )

        return detailed_info, best_info

    @classmethod
    def part_totals(cls):
        """
        How much of each body part do we mention?
        """
        def count_part(part):
            return sum(
                1 for card in Card.all_types.values()
                if part in card.get_description()
            )

        parts = sorted(list(Card.strike_targets.keys() | Card.hands))
        totals = {
            part: count_part(part) for part in parts
        }

        return (
            f"<div style='break-inside: avoid;'>{status_string(totals)}</div>"
        )

