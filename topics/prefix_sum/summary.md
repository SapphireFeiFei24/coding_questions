# Prefix Sum
## Templates
```python
def prefix_sum_1d(nums):
    res = [0 for i in range(len(nums) + 1)]
    for i in range(nums):
        res[i + 1] = res[i] + nums[i]
    return res
```
## Time Complexity
* Constructing the array: O(N)
* Query a range sum: O(1)
## Applications
### Range Sum
> Find a total sum of elements within a subarray.
```python
# (zero indexed)
def range_sum(prefix_sum_1d,start, end):
    # return the sum of [start, end)
    # prefix_sum_1d[end] = sum([0,end-1])
    # prefix_sum_1d[start] = sum([0,start-1])
    # sum of [start, end) = sum([0,end-1]) - sum([0,start-1])
    return prefix_sum_1d[end] - prefix_sum_1d[start]
```
### Range Operations
> Return the final result of the array after multiple range operations
> Example of range operation: add one for elements between [start, end)

The result array is a prefix sum over the array that records the operations.
```python
def range_op(changes, start, end, op):
    changes[start] += op
    changes[end] -= op

def result_after_range_ops(n, operations):
    changes = [0] * n
    for start, end, op in operations:
        range_op(changes, start, end, op)
    return get_prefix_sum_array(changes)
```
