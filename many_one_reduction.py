def subset_sum_to_knapsack(subset, target_sum):
    # convert sum to a knapsack instance
    n = len(subset)
    weights = [1] * n
    values = subset
    capacity = target_sum


    return n, capacity, weights, values


# example usage
subset = [3, 5, 7, 8]
target_sum = 15

knapsack_instance = subset_sum_to_knapsack(subset, target_sum)
print("knapsack distance: ", knapsack_instance)