# collection protocols

"""
container protocol (allows us to use 'in' and 'not in') -> str, list, range, set, dict, bytes, tuple

sized protocol (allows us to call the len(s) to check size) -> str, list, range, set, dict, bytes, tuple

iterable protocol (allows us to loop through a collection, can produce an iterator with iter(s))
    -> str, list, range, set, dict, bytes, tuple

sequence protocol (allows us random read access to collections, allows us to retrieve elements by index -> seq[index],
find items by value -> seq.index(element), count items -> seq.count(element), produce a reversed seq -> reversed(seq))
    -> str, list, bytes, tuple, range

set protocol supports different set operations such as subset, superset, equal, not equal, proper subset
proper superset, intersections, union, difference, symmetric difference
    -> set

mutable sequence -> list
mutable set -> set
mutable mapping -> dict
"""
