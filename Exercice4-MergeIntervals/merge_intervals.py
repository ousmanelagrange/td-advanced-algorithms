def merge_intervals(intervals):
    if not intervals:
        return []

    # Étape 1 : Trier les intervalles par heure de début
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]

    for current in intervals[1:]:
        last_merged = merged[-1]

        # Vérifier si l'intervalle actuel chevauche le dernier intervalle fusionné
        if current[0] <= last_merged[1]:
            # Fusionner les deux intervalles
            merged[-1] = (last_merged[0], max(last_merged[1], current[1]))
        else:
            # Ajouter l'intervalle actuel à la liste fusionnée
            merged.append(current)

    return merged
