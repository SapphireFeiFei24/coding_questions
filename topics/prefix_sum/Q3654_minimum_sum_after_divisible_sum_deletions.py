'''
Description
You are given an integer array nums and an integer k.
You may repeatedly choose any contiguous subarray of nums whose sum is divisible by k and delete it; after each deletion, the remaining elements close the gap.
Return the minimum possible sum of nums after performing any number of such deletions.

Intuition:
Superpower combining prefixsum with modular:
A subarray sum is divisible by k precisely when the prefix sums at its two endpoints have the same remainder mod k.

Technique:
prefix sum + dynamic programming
'''
import sys
class Solution:
    def minArraySum(self, nums: List[int], k: int) -> int:
        # preprocess: get prefix sum -- O(N)
        prefix_sum = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]

        # Main dp logic: for each step, consider keep or delete -- O(N)
        dp = [0] + [sys.maxsize for i in nums]
        last = {}
        last[0] = -1
        for i in range(len(nums)):
            val = prefix_sum[i + 1] % k
            dp[i + 1] = min(dp[i + 1], dp[i] + nums[i])
            if val in last:
                idx = last[val]
                dp[i + 1] = min(dp[i + 1], dp[idx + 1])
            # Attention: always update the last val with the latest position
            last[val] = i
        return dp[-1]