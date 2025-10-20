"""
Euclidean Algorithm
gcd(a,b) = gcd(b, a mod b)
where b == 0, gcd(a,0) == abs(a)

Time Complexity = O(log(min(a,b)))
"""

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return abs(a)


# One liner
import math
def gcd_builtin(a,b):
    return math.gcd(a, b)


# For multiple numbers
from functools import reduce
def gcd_multiple(numbers: list[int]) -> int:
    return reduce(math.gcd, numbers)


