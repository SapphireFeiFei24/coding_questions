"""
    Dynamic Programming
    
    Main Idea:
        * Define subproblems
        * Find the base problem
        * Find the relationship between the problem and subproblems
        * Use memorization to \
                efficiently store the result of the subproblems.
"""
# Recursive Solution -----------------------------------------------
memo = {}
def dp_recursive(x):
    # base problem
    if x == 0:
        return res
    # if already calculated
    if x in memo.keys():
        return memo[x]
    res = sys.maxsize # or 0 if looking for the maximum
    for sub in subproblems:
        res = min(res, dp_recursive(sub) + k)
    memo[x] = res
    return res

# Iterative Solution ----------------------------------------------
def dp_iterative(n, nums):
    # res[0] as the base problem
    res = [0 for i in range(n + 1)]
    for i in range(1, range(n + 1):
        res[i] = res[i - 1] # or other default val
        for sub in subproblems:
            res[i] = min(res[i], res[sub] + k)
    return res[-1]

