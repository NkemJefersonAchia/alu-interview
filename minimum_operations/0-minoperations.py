#!/usr/bin/python3
def minOperations(n):
    """
    Calculates the fewest number of operations needed to result in
    exactly n H characters in the file.
    
    Args:
        n: target number of H characters
    
    Returns:
        Minimum number of operations, or 0 if impossible
    """
    if n <= 1:
        return 0
    
    operations = 0
    divisor = 2
    
    # Find all prime factors and sum them
    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n = n // divisor
        divisor += 1
    
    return operations
