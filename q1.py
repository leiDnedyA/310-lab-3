from typing import List

def findAllSquares(n: int) -> List[int]:
    if n < 1:
        return []
    if n == 1:
        return [1]
    return [i**2 for i in range(1, int(n**.5))]

def numSquares(n: int) -> int:
    """
    Find the fewest number of perfect square numbers
    that can be added together to get n
    """
    return findAllSquares(n)
    

if __name__ == "__main__":
    print(numSquares(12))
