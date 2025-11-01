"""
Description:
Design a data structure to store the strings' count with the ability to return the strings with minimum and maximum counts.
Implement the AllOne class:
AllOne() Initializes the object of the data structure.
inc(String key) Increments the count of the string key by 1. If key does not exist in the data structure, insert it with count 1.
dec(String key) Decrements the count of the string key by 1. If the count of key is 0 after the decrement, remove it from the data structure. It is guaranteed that key exists in the data structure before the decrement.
getMaxKey() Returns one of the keys with the maximal count. If no element exists, return an empty string "".
getMinKey() Returns one of the keys with the minimum count. If no element exists, return an empty string "".
Note that each function must run in O(1) average time complexity.
"""

'''
Solution 1
hashmap alone. Worse case is O(N)
'''
class AllOne:

    def __init__(self):
        self.curr_max = 0
        self.curr_min = 0
        self.freq_key = defaultdict(set)
        self.key_freq = {}

    def inc(self, key: str) -> None:
        if key not in self.key_freq:
            self.key_freq[key] = 0
        self.key_freq[key] += 1

        # move this key up one ladder
        freq = self.key_freq[key]
        self.freq_key[freq].add(key)
        if freq - 1 > 0:
            self.freq_key[freq - 1].remove(key)

        # update max
        if freq > self.curr_max:
            self.curr_max = freq

        # update min: when the current becomes the new min or there's no more ele in the lowest bucket
        if (freq and freq < self.curr_min) or len(self.freq_key[self.curr_min]) == 0:
            self.curr_min = freq
        # print("inc", key, self.freq_key, self.curr_max, self.curr_min)

    def dec(self, key: str) -> None:
        self.key_freq[key] -= 1
        freq = self.key_freq[key]

        # move this key down one ladder
        self.freq_key[freq + 1].remove(key)
        if freq:
            self.freq_key[freq].add(key)

        # update curr_max
        if len(self.freq_key[self.curr_max]) == 0:
            self.curr_max -= 1

        # update curr_min
        if freq and freq < self.curr_min:  # if it becomes the new min
            self.curr_min = freq
        elif len(self.freq_key[self.curr_min]) == 0:
            # if curr min is empty, min need to move up the find the new min(worse case O(N))
            new_min = sys.maxsize
            for k in self.freq_key:
                if len(self.freq_key[k]):
                    new_min = min(k, new_min)
            if new_min == sys.maxsize:
                self.curr_min = -1
            else:
                self.curr_min = new_min
        # print("dec", key, self.freq_key, self.curr_max, self.curr_min)

    def getMaxKey(self) -> str:
        data = self.freq_key[self.curr_max]
        # print("get_max", self.curr_max, data)
        if not data:
            return ""
        return next(iter(data))

    def getMinKey(self) -> str:
        data = self.freq_key[self.curr_min]
        # print("get_min", self.curr_min, data)
        if not data:
            return ""
        return next(iter(data))


'''
Approach 2: Hashmap + Double Linked List
'''
class Node:
    def __init__(self, freq):
        self.prev = None
        self.next = None
        self.ele = set()  # set of elements with same freq
        self.freq = freq


class AllOne:
    def __init__(self):
        self.key_node = {}
        self.head = Node(0)
        self.tail = Node(sys.maxsize)
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_node(self, new_node, prev, after):
        new_node.prev = prev
        new_node.next = after
        prev.next = new_node
        after.prev = new_node

    def remove_node(self, node):
        prev, after = node.prev, node.next
        prev.next = after
        after.prev = prev

    def move_up(self, node, key):
        node.ele.remove(key)
        node.next.ele.add(key)

    def move_down(self, node, key):
        node.ele.remove(key)
        node.prev.ele.add(key)

    def inc(self, key: str) -> None:
        # two scenarios: next node exist/next node not exist
        init_node = None
        if key not in self.key_node:
            self.head.ele.add(key)  # init from head
            init_node = self.head
        else:
            init_node = self.key_node[key]

        if init_node.next.freq != init_node.freq + 1:  # create a new node
            new_node = Node(init_node.freq + 1)
            self.add_node(new_node, init_node, init_node.next)  # insert after init_node
        self.move_up(init_node, key)
        if not init_node.ele and init_node != self.head:
            self.remove_node(init_node)
        self.key_node[key] = init_node.next

    def dec(self, key: str) -> None:
        init_node = self.key_node[key]  # guaranteed calling after inc

        if init_node.prev.freq != init_node.freq - 1:
            new_node = Node(init_node.freq - 1)
            self.add_node(new_node, init_node.prev, init_node)  # insert before init node

        self.move_down(init_node, key)
        self.key_node[key] = init_node.prev

        if not init_node.ele:
            self.remove_node(init_node)
        # clear if it's zero
        if self.key_node[key] == self.head:
            del self.key_node[key]
            self.head.ele.remove(key)

    def getMaxKey(self) -> str:
        if not self.tail.prev.ele:
            return ""
        return next(iter(self.tail.prev.ele))

    def getMinKey(self) -> str:
        if not self.head.next.ele:
            return ""
        return next(iter(self.head.next.ele))

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
