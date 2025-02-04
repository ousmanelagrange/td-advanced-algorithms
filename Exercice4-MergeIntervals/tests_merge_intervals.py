import unittest
from merge_intervals import merge_intervals

class TestMergeIntervals(unittest.TestCase):
    def test_no_overlap(self):
        intervals = [(1, 3), (5, 7), (8, 10)]
        result = merge_intervals(intervals)
        self.assertEqual(result, [(1, 3), (5, 7), (8, 10)])

    def test_partial_overlap(self):
        intervals = [(1, 5), (2, 6), (8, 10)]
        result = merge_intervals(intervals)
        self.assertEqual(result, [(1, 6), (8, 10)])

    def test_full_overlap(self):
        intervals = [(1, 10), (2, 3), (4, 8)]
        result = merge_intervals(intervals)
        self.assertEqual(result, [(1, 10)])

    def test_empty_list(self):
        intervals = []
        result = merge_intervals(intervals)
        self.assertEqual(result, [])

    def test_single_interval(self):
        intervals = [(2, 5)]
        result = merge_intervals(intervals)
        self.assertEqual(result, [(2, 5)])

if __name__ == '__main__':
    unittest.main()
