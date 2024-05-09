from typing import List
from math import sqrt, floor

def numSquares(n: int) -> int:
    """
    Find the fewest number of perfect square numbers
    that can be added together to get n
    """
    if n <= 3:
        return n
    result = n
    for x in range(1, floor(sqrt(n)) + 1):
        sq = x**2
        potentialResult = 1 + numSquares(n - sq)
        result = min(result, potentialResult)
    return result
    

if __name__ == "__main__":
    print(numSquares(12))
