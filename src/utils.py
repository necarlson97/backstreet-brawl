import re
from abc import ABCMeta

"""
Module of handy utilities
"""

# TODO clamp

def camel_to_hypens(text):
    return re.sub('([a-z0-9])([A-Z])', '\\1-\\2', text).lower()

def snake_to_title(text):
    return (
        ' '.join(word.title() for word in re.split('[_-]', text) if word)
    )

def status_string(item):
    # Simple helper function for +1/-1, etc
    if isinstance(item, dict):
        return "".join(f"<div>{status_string(i)}</div>" for i in item.items())
    k, v = item
    if v == 0:
        return ""
    sign = f"<span class='minus'>{v}</span>"
    if v > 0:
        sign = f"<span class='plus'>+{v}</span>"
    return f"<span class='{k} status'>{sign} {k}</span>"

def get_cost_from_menu(menu, source):
    """
    Take a 'menu' dict of keywords and how they will effect 'cost',
    and a 'source' text, and return a dict of:
    parts of the source string that were pertinent => how it effected cost
    """
    and_parts = [part.strip() for part in source.split('and')]
    pertinent_costs = {}

    def get_min_cost_or(part):
        or_parts = [p.strip() for p in part.split('or ')]
        min_cost = float('inf')
        min_part = None
        for op in or_parts:
            for k, v in menu.items():
                if k.lower() in op.lower():
                    if abs(v) < min_cost:
                        min_cost = v
                        min_part = f"{k} ({op})"
        return (
            min_cost if min_cost != float('inf') else 0,
            min_part if min_part else None
        )

    def get_sum_cost_and(part):
        cost = 0
        matched_parts = []
        for k, v in menu.items():
            if k.lower() in part.lower():
                cost += v
                matched_parts.append(f"{k} ({part})")
        return cost, matched_parts

    for part in and_parts:
        cost, matched_part = get_min_cost_or(part)
        if matched_part:
            pertinent_costs[matched_part] = cost
        else:
            cost, matched_parts = get_sum_cost_and(part)
            for matched_part in matched_parts:
                pertinent_costs[matched_part] = cost

    return pertinent_costs

def get_range(range_a, range_b=None):
    """
    Given a min and max, return a tuple of min, max.
    If a single tuple argument is given, return it.
    If two arguments are given, order them and return as (min, max).
    """
    if isinstance(range_a, tuple):
        return range_a
    else:
        if range_b is not None:
            return (min(range_a, range_b), max(range_a, range_b))
        else:
            return (0, range_a)

class NamedClassMeta(type):
    """
    Just a little helper metaclass to keep track of each types name
    even without instantiation
    """
    def __new__(cls, name, bases, dct):
        new_class = super().__new__(cls, name, bases, dct)
        new_class.name = camel_to_hypens(name)
        return new_class

class CombinedNameMeta(ABCMeta, NamedClassMeta):
    """
    In case we want to define a child class as abstract, this lets us use
    ABC alongside our custom named class metaclass
    """
    pass

class NamedClass(metaclass=CombinedNameMeta):
    """
    Parent class that help keep track of the names of a type with many
    subtypes (such as cards, mechs, etc)
    """

    @classmethod
    def human_name(cls):
        return snake_to_title(cls.name)

    @classmethod
    def short_name(cls):
        # 1s word plus 1st letter of next word
        words = cls.name.split('-')
        if len(words) == 1:
            return words[0]
        return words[0].title() + cls.name.split('-')[1][0].title()

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return self.__str__()

    # A dict that holds all defined subtypes by:
    # string of class name -> type
    # (just for checking name conflicts)
    all_named_types = {}
    @classmethod
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        # Register each subclass in the all_cards dictionary
        cls.all_named_types[cls.__name__] = cls
        # TODO check for conflict here
