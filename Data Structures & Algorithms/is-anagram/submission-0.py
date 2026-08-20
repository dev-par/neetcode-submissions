from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # same characters, same frequency
        # can't use a set because a character may appear more than once
        # could sort them, but that's O(nlogn)
        # use a counter for O(2n)
        s_count = Counter(s)
        t_count = Counter(t)

        return s_count == t_count