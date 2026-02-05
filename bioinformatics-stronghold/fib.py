"""
FIB: Rabbits and Recurrence Relations
Problem: Calculate rabbit population growth with reproduction factor.

Given: Positive integers n ≤ 40 and k ≤ 5.
Return: The total number of rabbit pairs that will be present after n months, 
        if we begin with 1 pair and in each generation, every pair of 
        reproduction-age rabbits produces a litter of k rabbit pairs.
"""


def fibonacci_rabbits(n: int, k: int):
    """
    Calculate rabbit population using modified Fibonacci sequence.
    
    Each pair of rabbits produces k pairs of offspring each generation.
    Uses recursive approach: F(n) = F(n-1) + k * F(n-2)
    
    Args:
        n (int): Number of months/generations
        k (int): Number of rabbit pairs produced per reproduction
        
    Returns:
        int: Total number of rabbit pairs after n months
    """
    # Base cases: start with 1 pair, still 1 pair after first month
    if n == 1:
        result = 1
    elif n == 2: 
        result = 1
    else:
        # Recursive case: current pairs + k * reproducing pairs from 2 months ago
        result = fibonacci_rabbits(n - 1, k) + k * (fibonacci_rabbits(n - 2, k))
    
    return result
 

# Calculate and output the result
print(fibonacci_rabbits(34, 4))