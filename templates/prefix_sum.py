"""
    Prefix Sum
    Use Case:
        * calculate the sum of subarrays:
            * sum(i, j) = prefix_sum[j] - prefix_sum[i] # (i, j]
            * prefix_sum[i+1]: the prefix sum of subarray [0, i]
        * range operation
            * mark the range first
            * the prefix sum is the final result
"""
def prefix_sum_1d(nums):
    res = [0 for i in range(len(nums) + 1)]
    for i in range(nums):
        res[i + 1] = res[i] + nums[i]
    return res

def prefix_sum_2d(matrix):
    m, n = len(matrix), len(matrix[0])
    res = [[0 for i in range(n)] for j in range(m)]
    for i in range(m):
        row = 0
        for j in range(n):
            row += matrix[i][j]
            res[i][j] = row
            if i > 0:
                res[i][j] += res[i-1][j]
    return res
