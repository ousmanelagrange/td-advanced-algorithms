# Exercice 5 : Maximum Subarray Sum (Kadane’s Algorithm)

## Problème
Vous devez implémenter l'algorithme de Kadane pour trouver la somme maximale d'un sous-tableau contigu dans un tableau donné de prix d'actions (ou d'entiers).

## Algorithme
1. **Initialisation :**
   - Une variable `current_sum` pour suivre la somme du sous-tableau courant.
   - Une variable `max_sum` pour suivre la somme maximale observée jusqu'à présent.
   
2. **Itération à travers le tableau :**
   - À chaque itération, mettre à jour `current_sum` pour être soit l'élément actuel, soit la somme de l'élément actuel et `current_sum` précédent.
   - Si `current_sum` devient négatif, le réinitialiser à l'élément courant.
   - Mettre à jour `max_sum` si `current_sum` est plus grand que `max_sum`.

3. **Retourner `max_sum`** à la fin de l'itération.

## Complexité
- **Complexité en temps :** O(n), où n est la taille du tableau (nous passons une seule fois à travers le tableau).
- **Complexité en espace :** O(1), car nous n'utilisons que deux variables pour le suivi de la somme.

## Exemple de code :
```python
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result = max_subarray_sum(nums)
print(result)  # 6 (Sous-tableau [4, -1, 2, 1])

Cas de test :

    Tous les éléments sont positifs : Entrée : [1, 2, 3, 4, 5]
    Sortie : 15

    Tous les éléments sont négatifs : Entrée : [-1, -2, -3, -4, -5]
    Sortie : -1

    Éléments mixtes : Entrée : [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    Sortie : 6

    Un seul élément : Entrée : [10]
    Sortie : 10

    Tableau vide : Entrée : []
    Sortie : -inf (pas de sous-tableau dans un tableau vide)

Conclusion

L'algorithme de Kadane est une solution efficace pour trouver la somme maximale d'un sous-tableau contigu. Il est particulièrement utile dans des applications financières où vous devez analyser des séquences de valeurs changeantes.

Analyse de la complexité temporelle de l'algorithme de Kadane et comparaison avec une approche brute-force
Kadane's Algorithm :

    Complexité en temps : O(n)
    L'algorithme de Kadane parcourt le tableau une seule fois (en une seule passe) pour trouver la somme maximale d'un sous-tableau contigu. À chaque élément, il met à jour la somme du sous-tableau actuel et la somme maximale observée, ce qui prend un temps constant pour chaque itération. Donc, le temps total est directement proportionnel à la taille du tableau, d'où la complexité O(n).

    Complexité en espace : O(1)
    Kadane's algorithm n'utilise que quelques variables auxiliaires pour suivre la somme actuelle et la somme maximale. Il ne nécessite pas d'espace supplémentaire proportionnel à la taille de l'entrée, donc la complexité spatiale est O(1).

Approche brute-force (Force brute) :

    Complexité en temps : O(n²)
    L'approche brute-force consiste à générer tous les sous-tableaux possibles du tableau et à calculer la somme de chaque sous-tableau pour déterminer celui avec la somme maximale. Si le tableau contient nn éléments, il y a n(n+1)22n(n+1)​ sous-tableaux possibles (ce qui donne une complexité quadratique). Pour chaque sous-tableau, le calcul de la somme prend un temps proportionnel à la taille du sous-tableau, ce qui donne une complexité totale de O(n²).

    Complexité en espace : O(1) (en considérant que nous ne stockons pas les sous-tableaux explicitement, mais seulement les sommes).

Comparaison :

    Kadane's algorithm est beaucoup plus efficace avec une complexité en temps O(n), ce qui le rend adapté pour des tableaux de grande taille. Il résout le problème en une seule passe.

    Approche brute-force est beaucoup plus lente avec une complexité en temps O(n²). Bien qu'elle soit plus facile à comprendre et à implémenter, elle devient impraticable pour de grands ensembles de données en raison de la croissance quadratique du temps d'exécution.

Résumé :

    Kadane's algorithm : Temps O(n)O(n), espace O(1)O(1).
    Approche brute-force : Temps O(n2)O(n2), espace O(1)O(1).

Kadane's algorithm est nettement plus efficace et préféré dans des cas pratiques, surtout lorsqu'il s'agit de traiter de grandes quantités de données.