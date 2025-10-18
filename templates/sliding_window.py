"""
    Sliding Window/Two Pointers
    Main Idea:
    * right - left: the max length of valid sequences so far.
    * For each loop:
        1. update k according to right
        2. if condition becomes invalid:
            2.1 update k accoding to left
            2.2 move forward left pointer
        3. move forward right pointer # always
    Note:
    * The subsequence [left:right+1] is not always valid,
        it's just a length of current max valid seqence.
            
"""
def longestOnes(nums: List[int], k: int) -> int:
    left, right = 0, 0
    while right < len(nums):
        # if adding in nums[right] triggers the update of k
        if nums[right] == 0:
            k -= 1
        # if the condition becomes invalid, update left
        if k < 0:
            # if removing nums[left] triggers the update of k
            if nums[left] == 0:
                k += 1
            left += 1
        right += 1
    return right - left
