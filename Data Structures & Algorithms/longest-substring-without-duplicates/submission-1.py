from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # what does without duplicate characters mean
        # if we have a counter, the freq can be one max
        # have a left and right pointer
        # iterate right pointer until the condition is broken
        # when condition is broken, iterate left pointer until it's met again
        best_length = 0
        seen = set()
        l, r = 0, 0
        while r < len(s):
            # shrink window until it's out of seen
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            best_length = max(best_length, (r - l) + 1)
            r += 1
        return best_length

        # zxyzxyz
        #     l
        #       r
        # 0123456 
