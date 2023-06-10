# https://leetcode.com/problems/sliding-window-maximum/description/
# Got asked more than once/failed more than once on this problem
"""
    deque[0] to be the index of the max val.
    Each time:
    - popleft the invalid indexes
    - popright the ones that are smaller than the one that's about to push in
    - get nums[deque[0]]"
"""
# Time complexity O(n)
# Space complexity O(n)
class Solution:
    # Solution 1 --------- max heap
    # def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    #     maxHeap = []
    #     count = {}
    #     for i in range(k):
    #         if nums[i] not in count.keys():
    #             count[nums[i]] = 0
    #             heapq.heappush(maxHeap, -nums[i])
    #         count[nums[i]] += 1
    #     res = [-maxHeap[0]]
    #     for i in range(len(nums)-k):
    #         left = nums[i]
    #         right = nums[i + k]
    #         count[left] -= 1
    #         while maxHeap and count[-maxHeap[0]] == 0:
    #             heapq.heappop(maxHeap)
    #         if right not in count.keys():
    #             count[right] = 0
    #         if count[right] == 0:  
    #             heapq.heappush(maxHeap, -right)
    #         count[right] += 1
    #         res.append(-maxHeap[0])
    #     return res

    # Solution 2 deque
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        for i in range(k):
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()
            dq.append(i)
        res = [nums[dq[0]]]
        for i in range(len(nums)-k):
            # print(i, dq)
            while dq and dq[0] <= i:
                dq.popleft()
            # print("after popleft", dq)
            j = i + k
            while dq and nums[dq[-1]] <= nums[j]:
                dq.pop()
            # print("after popright", dq)
            dq.append(j)
            # print("after append", dq)
            res.append(nums[dq[0]])
        return res

