"""
https://leetcode.com/problems/word-ladder/description/

Category:
    BFS
    String/char
NOTE: Naively generating graph by computing the distance between words will TLE
    * 1 <= len(wordList) <= 5000
    * O(n^2) = 5 * 10 ^ 6
    * Solution: make use of the fix space of alphabet(26) brute force in that space.

Time Complexity:
    O(n*26*10)
Space Complexity:
    O(n)

"""
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        dist_dict = {}
        def get_other_chars(char):
            return char_set - set([char])
        def connected_words(word):
            res = []
            for i in range(len(word)):
                other_chars = get_other_chars(word[i])
                for c in other_chars:
                    r = word[:i] + c + word[i+1:]
                    res.append(r)
            return res
        char_set = set([chr(i) for i in range(ord('a'), ord('z') + 1)])
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        dist = 1
        visited = set()
        curr_layer = set([beginWord])
        while curr_layer and endWord not in curr_layer:
            next_layer = set()
            for src in curr_layer:
                visited.add(src)
                for word in connected_words(src):
                    if word == endWord:
                        return dist + 1
                    if word in wordSet and word not in visited:
                        next_layer.add(word)
            dist += 1
            curr_layer = next_layer
        return 0

