# https://leetcode.com/problems/product-of-array-except-self/
# Category: prefix(suffix) sum
# Time Complexity: O(n)
# Space Complexity: O(1) (result arrary doesn't count as extra space)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1 for i in nums]
        # prefix
        for i in range(1, len(nums)):
            res[i] = nums[i-1] * res[i-1]
        right = 1
        # surffix
        for i in range(len(nums) - 2, -1, -1):
            res[i] *= right * nums[i+1]
            right *= nums[i+1]
        return res
