# https://leetcode.com/problems/minimum-size-subarray-sum/
# Category: subarray/two pointers
# Time Complexity: O(n)
# Space Complexity: O(1)

# Intuition: maintain a valid subarray
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, right = 0, 0
        curr = 0
        res = len(nums) + 1
        while right < len(nums):
            curr += nums[right]
            while left < len(nums) and curr - nums[left] >= target:
                curr -= nums[left]
                left += 1
            if curr >= target:
                res = min(res, right - left + 1)
            right += 1
        if res > len(nums):
            return 0
        return res
