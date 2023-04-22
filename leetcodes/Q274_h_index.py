
# Category: heap/hashmap
# https://leetcode.com/problems/h-index/
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        heapCount = []
        counts = collections.defaultdict(lambda:0)
        for c in citations:
            counts[c] += 1
            if counts[c] == 1:
                heapq.heappush(heapCount, -c)
        countPapers = 0
        res = 0
        while heapCount :
            c = -heapq.heappop(heapCount)
            countPapers += counts[c]
            res = max(res, min(c, countPapers))

        return res


