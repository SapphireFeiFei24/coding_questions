# https://leetcode.com/problems/maximum-69-number/description/
# Time complextiy: O(n)
# Space Complexity: O(n)
class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        reversed = 0
        while num:
            reversed = reversed * 10 + num % 10
            num = num // 10
        res = 0
        flipped = False
        while reversed:
            digit = reversed % 10
            if digit == 6 and not flipped:
                digit = 9
                flipped = True
            res = res * 10 + digit
            reversed = reversed // 10
        return res
