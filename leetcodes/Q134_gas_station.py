# https://leetcode.com/problems/gas-station/description/
# There're two ways to solve the problem
# 1. Two Pointers
#    Time Complexity: O(n)
#    Space Complexity: O(n)
# 2. One time scan
#    Time Complexity: O(n)
#    Space Complexity: O(1)

# Two Pointers --------------------------------
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        delta = [gas[i] - cost[i] for i in range(len(gas))]
        start = 0
        res = 0
        while start < len(delta):
            if res + delta[start] >= 0:
                res += delta[start]
                end = (start + 1) % len(delta)
                while res  >= 0:
                    res += delta[end]
                    if end == start:
                        return start
                    end += 1
                    end %= len(delta)
                while start < len(delta) and res < 0:
                    res -= delta[start]
                    start += 1
            else:
                start += 1
        return -1

# One time scan -------------------------------
class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:

        if sum(gas) < sum(cost): return -1   #   Example: gas = [1,2,3,4,5]  cost = [3,4,5,1,2]
                                             #
        tank = idx = 0                       #   i  gas  cost   tank        start
                                             #  ––– –––  ––––   –––––––––   –––––
        for i in range(len(gas)):            #   start = 0              0     0
                                             #   0   1    3    0+1-3 = -2     1    reset tank to 0, start to 0+1 = 1
            tank+= gas[i]-cost[i]            #   1   2    4    0+2-4 = -2     2    reset tank to 0, start to 1+1 = 2
            if tank < 0: tank, idx = 0, i+1  #   2   3    5    0+3-5 = -2     3    reset tank to 0, start to 2+1 = 3
                                             #   3   4    1    0+4-1 =  3     3
        return idx                           #   4   5    2    3+5-2 =  6     3
                                             #
                                             #  See explanation in problem description to verify that i = 3 works
