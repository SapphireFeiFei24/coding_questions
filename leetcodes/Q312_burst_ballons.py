"""
https://leetcode.com/problems/burst-balloons/description/
Category: DP
Main Idea:
    If the subproblem cannot be separated, try "reversed" order
Time Complexity: O(n^2)
Space Complexity: O(n^2)
"""

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        memo = {}
        nums = [1] + nums + [1]
        def dp(start, end): # [start, end)
            if start == end:
                return 0
            key = (start, end)
            if key in memo.keys():
                return memo[key]
            res = 0
            factor = nums[start-1] * nums[end]
            for i in range(start, end):
                coins = nums[i] * factor
                r = coins + dp(start, i) + dp(i+1, end)
                res = max(res, r)
            memo[key] = res
            return res
        return dp(1, len(nums)-1)
