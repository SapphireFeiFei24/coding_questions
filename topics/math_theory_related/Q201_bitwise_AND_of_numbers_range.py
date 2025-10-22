"""
Description:
Given two integers left and right that represent the range [left, right], return the bitwise AND of all numbers in this range, inclusive.

Intuition:
1. Result of range AND is the common prefix of the numbers
2. Common prefix of a range is the same as common prefix between the starting and ending number
3. How to find common prefix: bits shift to right until both become equal.

Complexity:
Time: O(1) bound by the bit length of integer
"""
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift = 0
        while left != right:
            left >>= 1
            right >>= 1
            shift += 1
        return left << shift
