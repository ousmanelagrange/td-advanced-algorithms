# Exercice 3 : Knapsack Problem (Problème du sac à dos)

## Problème
Le problème du sac à dos consiste à maximiser la valeur totale des objets que l'on peut mettre dans un sac à dos de capacité limitée, chaque objet ayant un poids et une valeur.

## Solution
L'algorithme utilisé ici est basé sur la **programmation dynamique**. Il calcule la valeur maximale que l'on peut obtenir pour chaque capacité du sac à dos jusqu'à la limite spécifiée.

### Exemple de code :
```python
max_weight = 50
weights = [10, 20, 30]
values = [60, 100, 120]
print(knapsack(max_weight, weights, values))  # 220

Explication de l'algorithme

    Étape 1 : Créer une matrice dp où chaque cellule représente la valeur maximale possible pour une capacité donnée.
    Étape 2 : Remplir la matrice en comparant la valeur d'inclure ou d'exclure un objet à chaque étape.
    Étape 3 : La valeur optimale se trouve à dp[n][max_weight], où n est le nombre d'objets.

Résultats
Exemple d'entrée :

    Capacité maximale : 50
    Poids des objets : [10, 20, 30]
    Valeurs des objets : [60, 100, 120]

Exemple de sortie :

Valeur maximale : 220
Conclusion

L'approche par programmation dynamique permet de résoudre efficacement le problème du sac à dos avec une complexité en temps de O(n * max_weight) et une complexité en espace de O(n * max_weight).