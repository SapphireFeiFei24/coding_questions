"""
https://leetcode.com/problems/increment-submatrices-by-one/description/

Category:
    2D prefix sum
Time Complexity:
    O(n^2)
Space Complextiy:
    O(n^2)
"""
class Solution(object):
    def rangeAddQueries(self, n, queries):
        """
        :type n: int
        :type queries: List[List[int]]
        :rtype: List[List[int]]
        """
        res = [[0 for i in range(n)] for j in range(n)]
        for r1, c1, r2, c2 in queries:
            res[r1][c1] += 1
            if r2 + 1 < n:
                res[r2 + 1][c1] -= 1
            if c2 + 1 < n:
                res[r1][c2 + 1] -= 1
            if r2 + 1 < n and c2 + 1 < n:
                res[r2 + 1][c2 + 1] += 1
        for i in range(n):
            row = 0
            for j in range(n):
                row += res[i][j]
                res[i][j] = row
                if i > 0:
                    res[i][j] += res[i-1][j]
        return res
