# Exercice 2: Graph Traversal (BFS et DFS)

## Problème
Vous travaillez sur un système de navigation pour une carte de ville. L'objectif est d'explorer les connexions entre différents emplacements en utilisant les algorithmes de parcours en largeur (BFS) et en profondeur (DFS).

## Solution
L'algorithme de **Breadth-First Search (BFS)** explore les nœuds niveau par niveau en utilisant une file d'attente.  
L'algorithme de **Depth-First Search (DFS)** explore les nœuds aussi profondément que possible avant de revenir en arrière.

### Exemple de code :
#### BFS :
```python
graph = Graph()
graph.add_edge(1, 2)
graph.add_edge(1, 3)
print(graph.bfs(1))  # [1, 2, 3]

DFS :

graph = Graph()
graph.add_edge(1, 2)
graph.add_edge(1, 3)
print(graph.dfs(1))  # [1, 2, 3]

Résultats
Exemple d'entrée :

Graph avec les connexions suivantes :

    1 → 2
    1 → 3
    2 → 4
    2 → 5
    3 → 6
    3 → 7

Exemple de sortie :

BFS : [1, 2, 3, 4, 5, 6, 7]
DFS : [1, 2, 4, 5, 3, 6, 7]
Conclusion

Le parcours BFS est utile pour trouver le chemin le plus court, tandis que le DFS est plus adapté pour explorer toutes les connexions d'un graphe. Les deux algorithmes ont une complexité en temps de O(V + E).