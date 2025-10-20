'''
You are given an integer array nums of length n and a 2D integer array queries of size q, where queries[i] = [li, ri, ki, vi].
For each query, you must apply the following operations in order:

Set idx = li.
While idx <= ri:
Update: nums[idx] = (nums[idx] * vi) % (10^9 + 7).
Set idx += ki.
Return the bitwise XOR of all elements in nums after processing all queries.

Contrains
1 <= n == nums.length <= 10^5
1 <= nums[i] <= 109
1 <= q == queries.length <= 10^5
queries[i] = [li, ri, ki, vi]
0 <= li <= ri < n
1 <= ki <= n
1 <= vi <= 10^5
'''
from collections import defaultdict
import math


class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        N, B = len(nums), math.sqrt(len(nums)) + 1
        MOD = 10 ** 9 + 7

        def simple_update(nums, query):
            l, r, k, v = query
            for i in range(l, r + 1, k):
                nums[i] = (nums[i] * v) % MOD

        def get_modular_inverse(num, MOD):
            # This is based on the assumption that MOD is a prime
            return pow(v, MOD - 2, MOD)

            # Compress query into events

        events = defaultdict(lambda: [1] * N)
        for l, r, k, v in queries:
            if k > B:
                simple_update(nums, (l, r, k, v))
            else:
                # events[k][l] for nums[l], nums[l+k], ...., update with *events[k][l]
                events[k][l] = events[k][l] * v % MOD
                r2 = r + (k - (r - l) % k)  # r2 is the first idx that STOP update
                if r2 < N:
                    # inverse this operation
                    events[k][r2] = events[k][r2] * get_modular_inverse(v, MOD) % MOD

        # Perform based on "prefix sum"
        for k, row in events.items():
            # row[i] meaning: for nums[i], nums[i+k], ... till the end all multiply with row[i]
            for i in range(k):  # update for each position within the stride(block)
                cur = 1  # record the multiplier
                for j in range(i, N, k):  # update for the same position for each block
                    cur = cur * row[j] % MOD
                    nums[j] = nums[j] * cur % MOD

        # perform XOR on the result array
        ans = 0
        for x in nums:
            ans ^= x
        return ans


