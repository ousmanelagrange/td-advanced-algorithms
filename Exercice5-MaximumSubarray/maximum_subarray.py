def max_subarray_sum(nums):
    # Initialiser les variables pour Kadane's algorithm
    current_sum = 0
    max_sum = float('-inf')

    for num in nums:
        # Si current_sum devient négatif, on le réinitialise
        current_sum = max(num, current_sum + num)
        
        # Mettre à jour le max_sum si nécessaire
        max_sum = max(max_sum, current_sum)

    return max_sum
