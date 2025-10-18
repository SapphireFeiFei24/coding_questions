# https://leetcode.com/problems/longest-consecutive-sequence/description/
# Category: Set/Hashmap
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        memo = set()
        for n in nums:
            memo.add(n)
        res, r = 0, 0
        for n in nums:
            if n not in memo:
                continue
            r += 1
            next = n
            memo.remove(n)
            while next + 1 in memo:
                r += 1
                next += 1
                memo.remove(next)
            # print(n, memo, r)
            next = n
            while next - 1 in memo:
                r += 1
                next -= 1
                memo.remove(next)
            # print(n, memo, r)
            res = max(res, r)
            r = 0
        return res              
        
