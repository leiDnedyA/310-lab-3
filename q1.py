from typing import List
from math import sqrt, floor

def numSquares(n: int) -> int:
    """
    Find the fewest number of perfect square numbers
    that can be added together to get n
    """
    dp = [0, 1, 2, 3]
    for i in range(4, n + 1):
        dp.append(i)
        for x in range(1, floor(sqrt(i)) + 1):
            sq = x**2
            if sq > i:
                break
            dp[i] = min(dp[i], 1 + dp[i - sq])
    return dp[n]

    

if __name__ == "__main__":
    print(numSquares(12))
