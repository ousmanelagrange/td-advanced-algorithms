# Exercice 1: Binary Search  
## Problème  
Vous travaillez sur une application où vous devez rechercher rapidement un nombre spécifique dans une liste triée d'entiers. La recherche doit être la plus rapide possible.  

**Objectif :** Implémenter un algorithme de recherche binaire pour trouver une valeur cible dans une liste triée.  

## Instructions  
1. Implémentez l'algorithme de recherche binaire qui prend une liste triée et une valeur cible.  
2. L'algorithme doit retourner l'index de la cible si elle est trouvée, sinon -1.  
3. Testez votre algorithme avec différentes listes triées et valeurs cibles.  
4. Analysez la complexité temporelle de la recherche binaire et comparez-la à une recherche linéaire.  

## Solution  
L’algorithme de recherche binaire fonctionne selon le principe de **diviser pour régner**.  

```python
def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
Résultats

Voici quelques exemples de tests :

    Entrée : nums = [1, 3, 5, 7, 9, 11, 15], target = 5 → Sortie : 2
    Entrée : nums = [1, 3, 5, 7, 9, 11, 15], target = 6 → Sortie : -1


Conclusion

La recherche binaire est beaucoup plus efficace que la recherche linéaire pour des listes triées, avec une complexité temporelle de O(log n) contre O(n) pour la recherche linéaire.

