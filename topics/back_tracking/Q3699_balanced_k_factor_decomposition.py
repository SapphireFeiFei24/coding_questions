'''
Description:
Given two integers n and k, split the number n into exactly k positive integers such that the product of these integers is equal to n.
Return any one split in which the maximum difference between any two numbers is minimized. You may return the result in any order.

Time Complexity:
for each position the value can be [4, 10^5], k positions to consider
total possible states for back_track is 5*10^5

Optimization:
by using start, we ensure it's a non-decreasing order.
This will avoid duplications like [1, 6, 8] [6, 1, 8]
'''
import sys


class Solution:
    def minDifference(self, n: int, k: int) -> List[int]:
        curr_res = []
        curr_diff = sys.maxsize

        def back_track(start, n, k, res):
            nonlocal curr_diff, curr_res
            if k == 1:
                if n >= start:
                    res.append(n)
                    small = min(res)
                    big = max(res)
                    if big - small < curr_diff:
                        curr_res = res[:]
                        curr_diff = big - small
                    res.pop()
                return
            for i in range(start, n+1):
                if n % i == 0:
                    res.append(i)
                    back_track(i, n//i, k-1, res)
                    res.pop()
        back_track(1, n, k, [])
        return curr_res