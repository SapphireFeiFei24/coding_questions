"""
https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/description/

Category: Intervals
Time Complexity: O(n)
Space Complexity: O(n)

For each ballons:
    Add [start, -1, p] [end, 1, p] into list L
        where -1 1 indicates it's the start/end of a ballon
Sort list L from small to big (left to right)
Note: for those with same l[0], put the ones which l[1] == -1 in front of ones with l[1] == 1
      reason is that, when shoot at l[0], all of the ballons at that position can be bursted.
"""
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        def compare(a, b):
            if a[0] == b[0]:
                if a[1] < b[1]:
                    return 1
                return -1
            if a[0] < b[0]:
                return 1
            return -1
        ballons = []
        for p in range(len(points)):
            start, end = points[p]
            ballons.append([start, -1, p])
            ballons.append([end, 1, p])
        ballons = sorted(ballons, key=functools.cmp_to_key(compare))
        res = 0
        curr_ballons = set()
        # print(ballons)
        while ballons:
            x, flag, p = ballons.pop()
            if flag < 0:
                curr_ballons.add(p)
            else:
                if p in curr_ballons:
                    res += 1
                    curr_ballons.clear()
        return res
