# Sqrt Decomposition

## Definition
Sqrt Decomposition is a method/data structure to perform some common operations in O(sqrt(N)) instead of O(N).

**The basic idea of sqrt decomposition is preprocessing.**

## Approaches
### Simple version -- O(N)
* Divide the base task into sqrt(n) subtasks, for each subtasks, precalculate the result.
* To get the result, only "sum up" the results of the whole blocks within the range AND special sum for the two "tails"
### Mo's algorithm -- O((N+Q)sqrt(N))
> Idea: answer the queries in a special order based on the indices.

## Applications
* Range sum
* Range sum after updates
## Referrences
* [cp-algorithms](https://cp-algorithms.com/data_structures/sqrt_decomposition.html)