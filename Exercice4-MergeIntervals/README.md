# Exercice 4 : Merge Intervals

## Problème
Vous travaillez sur une application de calendrier qui doit fusionner les intervalles de temps qui se chevauchent pour organiser les événements. L'objectif est de renvoyer une liste d'intervalles fusionnés.

## Algorithme
1. **Trier les intervalles par heure de début.**
2. **Parcourir les intervalles triés et fusionner les intervalles qui se chevauchent.**
   - Si l'intervalle actuel chevauche le dernier intervalle fusionné, les fusionner.
   - Sinon, ajouter l'intervalle actuel à la liste fusionnée.
   
## Complexité
- **Complexité en temps :** O(n log n) à cause du tri initial.
- **Complexité en espace :** O(n) pour stocker les intervalles fusionnés.

## Exemple de code :
```python
intervals = [(1, 3), (2, 6), (8, 10), (15, 18)]
result = merge_intervals(intervals)
print(result)  # [(1, 6), (8, 10), (15, 18)]

Cas de test :

    A

    ucun chevauchement :
    Entrée : [(1, 3), (5, 7), (8, 10)]
    Sortie : [(1, 3), (5, 7), (8, 10)]

    Chevauchement partiel :
    Entrée : [(1, 5), (2, 6), (8, 10)]
    Sortie : [(1, 6), (8, 10)]

    Chevauchement total :
    Entrée : [(1, 10), (2, 3), (4, 8)]
    Sortie : [(1, 10)]

    Liste vide :
    Entrée : []
    Sortie : []

    Un seul intervalle :
    Entrée : [(2, 5)]
    Sortie : [(2, 5)]

Conclusion

L'algorithme de fusion des intervalles est utile pour résoudre des problèmes pratiques tels que la planification d'événements, la gestion des plages horaires et l'optimisation des plages de ressources.


