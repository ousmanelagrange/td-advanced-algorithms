import unittest
from bfs_dfs import Graph

class TestGraphTraversal(unittest.TestCase):
    def setUp(self):
        self.graph = Graph()
        self.graph.add_edge(1, 2)
        self.graph.add_edge(1, 3)
        self.graph.add_edge(2, 4)
        self.graph.add_edge(2, 5)
        self.graph.add_edge(3, 6)
        self.graph.add_edge(3, 7)

    def test_bfs(self):
        result = self.graph.bfs(1)
        self.assertEqual(result, [1, 2, 3, 4, 5, 6, 7])

    def test_dfs(self):
        result = self.graph.dfs(1)
        self.assertEqual(result, [1, 2, 4, 5, 3, 6, 7])

if __name__ == '__main__':
    unittest.main()
