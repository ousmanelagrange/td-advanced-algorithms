import unittest
from maximum_subarray import max_subarray_sum

class TestKadaneAlgorithm(unittest.TestCase):
    def test_all_positive(self):
        nums = [1, 2, 3, 4, 5]
        result = max_subarray_sum(nums)
        self.assertEqual(result, 15)

    def test_all_negative(self):
        nums = [-1, -2, -3, -4, -5]
        result = max_subarray_sum(nums)
        self.assertEqual(result, -1)

    def test_mixed_numbers(self):
        nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        result = max_subarray_sum(nums)
        self.assertEqual(result, 6)

    def test_single_element(self):
        nums = [10]
        result = max_subarray_sum(nums)
        self.assertEqual(result, 10)

    def test_empty_array(self):
        nums = []
        result = max_subarray_sum(nums)
        self.assertEqual(result, float('-inf'))  # Pas de sous-tableau dans un tableau vide

if __name__ == '__main__':
    unittest.main()
