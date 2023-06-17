"""
    Monotonous Stack
    Use case:
        For subarrays that contain i:
            Find the leftmost/rightmost index of the subarrays 
                where i is the min/max
    Usually remodel the problem into:
        for subarrays where i is the smallest/biggest:
            result = i * xxxxx
"""
def monotonous_stack(nums):
    left = [0 for i in nums]
    stack = [-1] # len(nums) if rightmost
    for i, x in enumerate(nums):
        while stack[-1] != -1 and stack[-1] > x:
            # change the second condition accordingly
            stack.pop()
        left[i] = stack[-1]
        stack.append(i)


