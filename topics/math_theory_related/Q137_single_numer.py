"""
Description:
Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.
You must implement a solution with a linear runtime complexity and use only constant extra space.

Constraints:
1 <= nums.length <= 3*10^4
-31 <= nums[i] <= 2^31 - 1 (It has negative numbers, and we can assume that it's represented in 2's complement)
Intuition:
For the original problem: every ele appears two times except one for one, we can use XOR(modulo 2 addtion)
As an extension of that, we can do modulo 3 addition on each bit
"""
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for shift in range(32):  # highest bit as sign bit
            bit_sum = 0
            for n in nums:
                bit_sum += (n >> shift) & 1
            res |= (bit_sum % 3) << shift
        if res >= 1 << 31: # meaning the highest bit is one
            res = res - (1 << 32)
        return res


"""
Single number |||
Description
All numbers appear two times except two number appear one time

How to find those two.

Intuition:
XOR: cancel all the numbers that appear two times
X&(-X): get the rightmost bit.
"""
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        total = 0
        for n in nums:
            total ^= n
        diff = total & (-total)  # the lowest diff bit between the two
        x = 0
        for n in nums:
            if n & diff:  # Y will be excluded because y & diff == 0
                # at the end only x will be visible coz all the others are canceled out
                x ^= n
        return [x, x ^ total]