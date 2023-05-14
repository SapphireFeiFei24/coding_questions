# https://leetcode.com/problems/maximal-square/description/
# Category: 
##         dp 
##         brute force with prefix sum
##         2D stack
# Space Complexity: O(mn)
# Time Complexity: O(mn)
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        res = 0
        nums = [[0 for j in range(len(matrix[0]))] for i in range(len(matrix)) ]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '1':
                    nums[i][j] = 1
                if i > 0 and j > 0 and nums[i][j]:
                    nums[i][j] += min([nums[i-1][j-1], nums[i-1][j], nums[i][j-1]])
                res = max(res, nums[i][j])
        return res ** 2

