from collections.abc import Sequence, Set
from bisect import bisect_left
from itertools import chain


class SortedSet(Sequence, Set):
    def __init__(self, items=None):
        # sorted always return a list irrespecitve of what was passed to it
        self._items = sorted(set(items)) if items is not None else []

    def __contains__(self, item):  # special method for the container protocol
        try:
            self.index(item)
            return True
        except ValueError:
            return False

    def __len__(self):  # special method for the sized protocol
        return len(self._items)

    def __iter__(self):  # special method for the iterable protocol
        # return iter(self._items) or
        for item in self._items:
            yield item

    def __getitem__(
        self, index
    ):  # sequence protocol for supporting item retrieval through indexing
        result = self._items[index]
        return SortedSet(result) if isinstance(index, slice) else result

    def __repr__(self):
        return "SortedSet({})".format(repr(self._items) if self._items else "")

    def __eq__(self, rhs):  # equality protocol
        if not isinstance(rhs, SortedSet):
            return NotImplemented
        return self._items == rhs._items

    def __ne__(self, rhs):  # inequality protocol
        if not isinstance(rhs, SortedSet):
            return NotImplemented
        return self._items != rhs._items

    def count(self, item):
        return int(item in self)

    def index(self, item):
        index = bisect_left(self._items, item)
        if (index != len(self._items) and (self._items[index] == item)):
            return index
        raise ValueError(f'{item} not found')

    def __add__(self, rhs):
        return SortedSet(chain(self._items, rhs._items))

    def __mul__(self, rhs): # rhs stands for right-hand-side
        return self if rhs > 0 else SortedSet()

    def __rmul__(self, lhs): # left-hand-side
        return self * lhs

    def issubset(self, iterable):
        return self <= SortedSet(iterable)

    def issuperset(self, iterable):
        return self >= SortedSet(iterable)

    def intersection(self, iterable):
        return self & SortedSet(iterable)

    def union(self, iterable):
        return self | SortedSet(iterable)

    def symmetric_difference(self, iterable):
        return self ^ SortedSet(iterable)

    def difference(self, iterable):
        return self - SortedSet(iterable)
