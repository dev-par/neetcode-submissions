class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # what are duplicate characters
        # if you place the characaters into a set the length is lesser
        # longest substring has a start and an end index we need to keep track of,
        # sounds like a sliding window problem 

        # what makes a valid window? we have a set with all characters inside the current
        # window. a window is valid if our current character isn't in the set yet. We can 
        # add it and recompute the window length. If the character is already in the set,
        # we iterate the left pointer and remove the character from the set. We do this 
        # until we remove the occurrence of the character we're adding

        if len(s) == 0:
            return 0

        longest_substring = 0
        chars = set()
        l = 0

        for r in range(len(s)):
            char = s[r]

            while l < r and char in chars:
                prev_char = s[l]
                chars.remove(prev_char)
                l += 1

            chars.add(char)
            new_length = r - l + 1
            longest_substring = max(longest_substring, new_length)

            r += 1
        
        return longest_substring
            
            
            

            


