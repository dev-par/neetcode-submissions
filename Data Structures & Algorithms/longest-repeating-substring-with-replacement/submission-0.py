from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # same idea as previous problem, but keep an integer for number of replacement
        # keep track of count of most frequent character, subtract window size from it
        most_freq_character_count = 0
        max_length = 0
        seen = defaultdict(int)
        l, r = 0, 0
        while r < len(s):
            char = s[r]
            seen[char] += 1
            most_freq_character_count = max(seen.values())
            # tentatively shrink window if char in seen
            while ((r - l + 1) - most_freq_character_count) > k and l < len(s):
                # shrink window
                seen[s[l]] -= 1
                l += 1

            # keep moving if char not in seen
            # in both cases add freq of char at right
            
            max_length = max(max_length, r-l+1)
            
            r += 1

        return max_length
