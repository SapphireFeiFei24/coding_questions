"""
https://leetcode.com/problems/non-overlapping-intervals/description/
Categories: Greedy; Interval Scheduling
Main Idea:
    Always pick the one with earliest ends
    Solution: https://leetcode.com/problems/non-overlapping-intervals/solutions/276056/python-greedy-interval-scheduling/
Time Complexity: O(nlogn)
Space Complexity: O(1)
"""
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        end, cnt = float('-inf'), 0
        for s, e in sorted(intervals, key=lambda x:x[1]):
            if s >= end:
                end = e
            else:
                cnt += 1
        return cnt
