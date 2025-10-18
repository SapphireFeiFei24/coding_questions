# https://leetcode.com/problems/sum-of-matrix-after-queries/description/
# Personally like this one >0<~~~
# Category: Don't know how..
# Time Complexity: O(n)
# Space Complexity: O(n)

# Intuition ----------------------
# Based on the observation that:
# res = 0 + q1 * n1 + q2 * n2 + .... + qk * nk
# where ni is the final actual number of cells affected by qi in the end

# ni can be easily calculated if the queries are processed backwards.

class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        nr, nc = n, n
        formulars = []
        is_row_changed = [False for i in range(n)]
        is_col_changed = [False for i in range(n)]
        for i in range(len(queries) - 1, -1, -1):
            t, idx, val = queries[i]
            if t == 0 and not is_row_changed[idx]:
                formulars.append([nr, val])
                is_row_changed[idx] = True
                nc -= 1
            elif t == 1 and not is_col_changed[idx]:
                formulars.append([nc, val])
                is_col_changed[idx] = True
                nr -= 1
        res = 0
        for f in formulars:
            res += f[0] * f[1]
        return res 
