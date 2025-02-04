import unittest
from knapsack import knapsack

class TestKnapsack(unittest.TestCase):
    def test_case_1(self):
        max_weight = 50
        weights = [10, 20, 30]
        values = [60, 100, 120]
        result = knapsack(max_weight, weights, values)
        self.assertEqual(result, 220)

    def test_case_2(self):
        max_weight = 10
        weights = [1, 2, 3]
        values = [10, 15, 40]
        result = knapsack(max_weight, weights, values)
        self.assertEqual(result, 65)

if __name__ == '__main__':
    unittest.main()
