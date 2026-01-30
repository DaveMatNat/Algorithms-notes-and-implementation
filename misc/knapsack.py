# items contains (value, weight) tuples for each item
# items[x][0] --> value of item x
# items[x][1] --> weight of item x

def knapSack(items: list, bag_cap: int, n: int):
    """
    Solves the 0/1 knapsack problem using recursion.
    
    Args:
        items: List of tuples where each tuple is (value, weight)
        bag_cap: Remaining capacity of the knapsack
        n: Number of items to consider (considers items[0] to items[n-1])
    
    Returns:
        Maximum value achievable with given capacity and items
    """
    
    # Base case: no items left or no capacity remaining
    if n == 0 or bag_cap == 0:
        return 0
    
    # If the current item is too heavy for remaining capacity, skip it
    # We can't include this item, so only consider the remaining n-1 items
    if items[n-1][1] > bag_cap:
        return knapSack(items, bag_cap, n-1)
    
    else:
        # Option 1: Include the current item
        # Add its value and recursively solve for remaining capacity and items
        includeItem = items[n-1][0] + knapSack(items, bag_cap - items[n-1][1], n - 1)

        # Option 2: Exclude the current item
        # Recursively solve with same capacity but one fewer item
        excludeItem = knapSack(items, bag_cap, n - 1)
        
        # Return whichever choice gives maximum value
        return max(includeItem, excludeItem)


# Test case: items with (value, weight) pairs
val_weights = [(20,8), (18,6), (4,3), (15,7), (5,1)]
C = 10  # Knapsack capacity
print(knapSack(val_weights, C, len(val_weights)))