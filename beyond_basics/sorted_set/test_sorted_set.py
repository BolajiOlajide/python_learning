import unittest
from collections.abc import Container, Sized, Iterable, Sequence, Set

from sorted_set import SortedSet


class TestSortedSetConstruction(unittest.TestCase):
    def test_empty(self):
        s = SortedSet([])

    def test_from_sequence(self):
        s = SortedSet([5, 2, 7, 1])

    def test_with_duplicates(self):
        s = SortedSet([2, 2, 3, 4])

    def test_with_generator(self):
        def generate_6432():
            yield 6
            yield 4
            yield 3
            yield 2

        g = generate_6432()
        s = SortedSet(g)

    def test_with_no_argument(self):
        s = SortedSet()


class TestSortedSetContainerProtocol(unittest.TestCase):
    def setUp(self):
        self.s = SortedSet([6, 7, 3, 9])

    def test_positive_contained(self):
        self.assertTrue(6 in self.s)

    def test_negative_contained(self):
        self.assertFalse(2 in self.s)

    def test_positive_not_contained(self):
        self.assertTrue(10 not in self.s)

    def test_negative_not_contained(self):
        self.assertFalse(9 not in self.s)

    def test_protocol(self):
        self.assertTrue(issubclass(SortedSet, Container))


class TestSortedSetSizedProtocol(unittest.TestCase):
    def test_empty(self):
        s = SortedSet()
        self.assertEqual(len(s), 0)

    def test_one(self):
        s = SortedSet([42])
        self.assertEqual(len(s), 1)

    def test_ten(self):
        s = SortedSet(range(10))
        self.assertEqual(len(s), 10)

    def test_with_duplicates(self):
        s = SortedSet([5, 5, 5])
        self.assertEqual(len(s), 1)

    def test_protocol(self):
        self.assertTrue(issubclass(SortedSet, Sized))


class TestSortedSetIterableProtocol(unittest.TestCase):
    def setUp(self):
        self.s = SortedSet([6, 7, 3, 9, 3])

    def test_iter(self):
        i = iter(self.s)
        self.assertEqual(next(i), 3)
        self.assertEqual(next(i), 6)
        self.assertEqual(next(i), 7)
        self.assertEqual(next(i), 9)
        self.assertRaises(StopIteration, lambda: next(i))

    def test_for_loop(self):
        index = 0
        expected = [3, 6, 7, 9]

        for item in self.s:
            self.assertEqual(item, expected[index])
            index += 1

    def test_protocol(self):
        self.assertTrue(issubclass(SortedSet, Iterable))


class TestSortedSetSequenceProtocol(unittest.TestCase):
    def setUp(self):
        self.s = SortedSet([6, 7, 3, 9, 3])

    def test_index_zero(self):
        self.assertEqual(self.s[0], 3)

    def test_index_three(self):
        self.assertEqual(self.s[3], 9)

    def test_index_error_is_raised_beyond_length(self):
        with self.assertRaises(IndexError):
            self.s[4]

    def test_index_minus_one(self):
        self.assertEqual(self.s[-1], 9)

    def test_index_minus_four(self):
        self.assertEqual(self.s[-4], 3)

    def test_index_error_negative_index_before_beginning(self):
        with self.assertRaises(IndexError):
            self.s[-5]

    def test_slice_from_start(self):
        self.assertEqual(self.s[:2], SortedSet([3, 6]))

    def test_slice_from_end(self):
        self.assertEqual(self.s[2:], SortedSet([7, 9]))

    def test_empty_slice(self):
        self.assertEqual(self.s[10:], SortedSet())

    def test_arbitrary_slice(self):
        self.assertEqual(self.s[1:3], SortedSet([6, 7]))

    def test_slice_full(self):
        self.assertEqual(self.s[:], self.s)

    def test_reversed(self):
        s = SortedSet([1, 3, 5, 7])
        # we could implement this with the __reversed__(self) method
        # but this makes use of the __getitem__ and __len__ if the __reversed__()
        # isn't defined, so we can do without it here.
        r = reversed(s)

        self.assertEqual(next(r), 7)
        self.assertEqual(next(r), 5)
        self.assertEqual(next(r), 3)
        self.assertEqual(next(r), 1)
        self.assertRaises(StopIteration, lambda: next(r))

    def test_index_positive(self):
        s = SortedSet([1, 5, 8, 9])
        self.assertEqual(s.index(8), 2)

    def test_index_negative(self):
        s = SortedSet([1, 5, 8, 9])
        self.assertRaises(ValueError, lambda: s.index(10))

    def test_count_zero(self):
        s = SortedSet([1, 5, 8, 9])
        self.assertEqual(s.count(11), 0)

    def test_count_one(self):
        s = SortedSet([1, 5, 8, 9])
        self.assertEqual(s.count(5), 1)

    def test_protocol(self):
        self.assertTrue(issubclass(SortedSet, Sequence))

    def test_concatenate_disjoint(self):
        s = SortedSet([1, 2, 3])
        t = SortedSet([4, 5, 6])
        self.assertEqual(s + t, SortedSet([1, 2, 3, 4, 5, 6]))

    def test_concatenate_equal(self):
        s = SortedSet([2, 4, 6])
        self.assertEqual(s + s, s)

    def test_concatenate_intersecting(self):
        s = SortedSet([1, 2, 3])
        t = SortedSet([3, 4, 5])
        self.assertEqual(s + t, SortedSet([1, 2, 3, 4, 5]))

    def test_multiplication_repition_zero_right(self):
        s = SortedSet([4, 5, 6])
        self.assertEqual(0 * s, SortedSet())

    def test_multiplication_repition_nonzero_right(self):
        s = SortedSet([4, 5, 6])
        self.assertEqual(100 * s, s)

    def test_multiplication_repition_zero_left(self):
        s = SortedSet([4, 5, 6])
        self.assertEqual(s * 0, SortedSet())

    def test_multiplication_repition_nonzero_left(self):
        s = SortedSet([4, 5, 6])
        self.assertEqual(s * 100, s)


class TestSortedSetReprProtocol(unittest.TestCase):
    def test_repr_empty(self):
        s = SortedSet()
        self.assertEqual(repr(s), "SortedSet()")

    def test_repr_non_empty_set(self):
        s = SortedSet([42, 40, 19])
        self.assertEqual(repr(s), "SortedSet([19, 40, 42])")


class TestSortedSetEqualityProtocol(unittest.TestCase):
    def test_positive_equal(self):
        self.assertTrue(SortedSet([4, 5, 6]) == SortedSet([4, 5, 6]))

    def test_negative_equal(self):
        self.assertFalse(SortedSet([4, 5, 6]) == SortedSet([1, 2, 3]))

    def test_type_mismatch(self):
        self.assertFalse(SortedSet([4, 5, 6]) == [4, 5, 6])

    def test_identical(self):
        s = SortedSet([10, 12, 11])
        self.assertTrue(s == s)


class TestSortedSetInequalityProtocol(unittest.TestCase):
    def test_positive_unequal(self):
        self.assertTrue(SortedSet([4, 5, 6]) != SortedSet([1, 2, 3]))

    def test_negative_unequal(self):
        self.assertFalse(SortedSet([4, 5, 6]) != SortedSet([6, 5, 4]))

    def test_type_mismatch(self):
        self.assertTrue(SortedSet([1, 2, 3]) != [1, 2, 3])

    def test_identical(self):
        s = SortedSet([10, 11, 12])
        self.assertFalse(s != s)


class TestSortedSetRelationalProtocol(unittest.TestCase):
    def test_lt_positive(self):
        s = SortedSet({1, 2})
        t = SortedSet({1, 2, 3})
        self.assertTrue(s < t)

    def test_lt_negative(self):
        s = SortedSet({1, 2, 3})
        t = SortedSet({1, 2, 3})
        self.assertFalse(s < t)

    def test_le_lt_positive(self):
        s = SortedSet({1, 2})
        t = SortedSet({1, 2, 3})
        self.assertTrue(s <= t)

    def test_le_eq_positive(self):
        s = SortedSet({1, 2, 3})
        t = SortedSet({1, 2, 3})
        self.assertTrue(s <= t)

    def test_le_negative(self):
        s = SortedSet({1, 2, 3})
        t = SortedSet({1, 2})
        self.assertFalse(s <= t)

    def test_gt_positive(self):
        s = SortedSet({1, 2, 3})
        t = SortedSet({1, 2})
        self.assertTrue(s > t)

    def test_gt_negative(self):
        s = SortedSet({1, 2})
        t = SortedSet({1, 2, 3})
        self.assertFalse(s > t)

    def test_ge_gt_positive(self):
        s = SortedSet({1, 2, 3})
        t = SortedSet({1, 2})
        self.assertTrue(s > t)

    def test_ge_eq_positive(self):
        s = SortedSet({1, 2, 3})
        t = SortedSet({1, 2, 3})
        self.assertTrue(s >= t)

    def test_ge_negative(self):
        s = SortedSet({1, 2})
        t = SortedSet({1, 2, 3})
        self.assertFalse(s >= t


        )


class TestSortedSetRelationalMethods(unittest.TestCase):
    def test_issubset_proper_positive(self):
        s = SortedSet({1, 2})
        t = [1, 2, 3]
        self.assertTrue(s.issubset(t))

    def test_issubset_positive(self):
        s = SortedSet({1, 2, 3})
        t = [1, 2, 3]
        self.assertTrue(s.issubset(t))

    def test_issubset_negative(self):
        s = SortedSet({1, 2, 3})
        t = [1, 2]
        self.assertFalse(s.issubset(t))

    def test_issuperset_proper_positive(self):
        s = SortedSet({1, 2, 3})
        t = [1, 2]
        self.assertTrue(s.issuperset(t))

    def test_issuperset_positive(self):
        s = SortedSet({1, 2, 3})
        t = [1, 2, 3]
        self.assertTrue(s.issuperset(t))

    def test_issuperset_negative(self):
        s = SortedSet({1, 2})
        t = [1, 2, 3]
        self.assertFalse(s.issuperset(t))


class TestSortedSetOperationSetProtocol(unittest.TestCase):
    def test_intersection(self):
        s = SortedSet({1, 2, 3})
        t = SortedSet({2, 3, 4})
        self.assertEqual(s & t, SortedSet({2, 3}))

    def test_union(self):
        s = SortedSet({1, 2, 3})
        t = SortedSet({2, 3, 4})
        self.assertEqual(s | t, SortedSet({ 1, 2, 3, 4}))

    def test_symmetric_difference(self):
        s = SortedSet({1, 2, 3})
        t = SortedSet({2, 3, 4})
        self.assertEqual(s ^ t, SortedSet({1, 4}))

    def test_difference(self):
        s = SortedSet({1, 2, 3})
        t = SortedSet({2, 3, 4})
        self.assertEqual(s - t, SortedSet({1}))


class TestSortedSetOperationSetMethod(unittest.TestCase):
    def test_intersection(self):
        s = SortedSet({1, 2, 3})
        t = [2, 3, 4]
        self.assertEqual(s.intersection(t), SortedSet({2, 3}))

    def test_union(self):
        s = SortedSet({1, 2, 3})
        t = [2, 3, 4]
        self.assertEqual(s.union(t), SortedSet({ 1, 2, 3, 4}))

    def test_symmetric_difference(self):
        s = SortedSet({1, 2, 3})
        t = [2, 3, 4]
        self.assertEqual(s.symmetric_difference(t), SortedSet({1, 4}))

    def test_difference(self):
        s = SortedSet({1, 2, 3})
        t = [2, 3, 4]
        self.assertEqual(s.difference(t), SortedSet({1}))

    def test_isdisjoint_positive(self):
        s = SortedSet({1, 2, 3})
        t = [4, 5, 6]
        self.assertTrue(s.isdisjoint(t))

    def test_isdisjoint_negative(self):
        s = SortedSet({1, 2, 3})
        t = [3, 4, 5]
        self.assertFalse(s.isdisjoint(t))


class TestSortedSetIsSetProtocol(unittest.TestCase):
    def test_protocol(self):
        self.assertTrue(issubclass(SortedSet, Set))


if __name__ == "__main__":
    unittest.main()
