"""
    Disjoint Set
    Use Case:
        find the connected graph
        clustering
    Two operations:
        * find: find which cluster this element belongs to
        * join: join two clusters
        * usual case: O(1)
        * worse case: O(n) # can be optimized
"""
roots = {} # key: element val: root
rank = collections.defaultdict(lambda:0)
def find(ele):
    if roots[ele] != ele:
        roots[ele] = find(roots[ele])
    return roots[ele]

def join(a, b):
    pA = find(a)
    pB = find(b)
    if rank[pA] > rank[pB]:
        roots[pB] = pA
    elif rank[pB] > rank[pA]:
        roots[pA] = pB
    else:
        roots[pA] = pB
        rank[pB] += 1
