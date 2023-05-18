# https://leetcode.com/problems/zigzag-conversion/description/
# Time Complexity: O(n)
# Space Complexity: O(s)
# Category: mapping
# Pay attention: the rows in the middle will have different delta iteratively
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        delta = 2*(numRows - 1)
        res = ""
        for i in range(numRows):
            idx = i
            d = delta
            if i != numRows - 1:
                d = delta - i * 2
            while idx < len(s):
                res += s[idx]
                idx += d
                if d != delta:
                    d = delta - d
        return res

