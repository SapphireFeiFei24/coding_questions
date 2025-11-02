"""
You are given a 0-indexed integer array nums and an integer value.

In one operation, you can add or subtract value from any element of nums.

For example, if nums = [1,2,3] and value = 2, you can choose to subtract value from nums[0] to make nums = [-1,2,3].
The MEX (minimum excluded) of an array is the smallest missing non-negative integer in it.

For example, the MEX of [-1,2,3] is 0 while the MEX of [1,0,3] is 2.
Return the maximum MEX of nums after applying the mentioned operation any number of times.

Intuition:
if a number % value == x, then non negative integer y where y % value == x can be created from num
"""
from collections import Counter
class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        freq = Counter([n % value for n in nums])

        x = 0
        while True:
            if freq[x % value] > 0:  # there's leftover unused num
                freq[x % value] -= 1
                x += 1
            else:
                return x