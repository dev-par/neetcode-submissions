from collections import Counter
class Solution:

    def valid_window(self, freq_t, freq_w):
        for char in freq_t:
            num_t = freq_t[char]
            num_w = freq_w[char]

            if num_w < num_t:
                return False
        
        return True


    def minWindow(self, s: str, t: str) -> str:
        # return the shortest substring of s such that every character in 
        # t is present in the substring

        # if that substring doesn't exist, return an empty string

        # return the actual substring, not just a length

        # how do we define a valid window here?

        # we have a counter for our substring and our target
        # every time we extend the window, we look for if the frequencies are
        # the same
        # we need to keep track of the max length and the indicies

        # expand the window until it's valid, shrink it until it isn't and
        # find the min. repeat until the end of the sequence

        min_length = float('inf')
        min_l = 0
        min_r = 0

        target_freq = Counter(t)
        window_freq = Counter()

        l, r = 0, 0
        while r < len(s):
            # expand the window until it's valid
            while r < len(s):
                if s[r] in target_freq:
                    window_freq[s[r]] += 1
                r += 1
                # print(f"Expanded window : {s[l:r]}")

                if self.valid_window(target_freq, window_freq):
                    # print("Window freq == target freq")
                    break
            
            # now either the window is valid or r is at the end of the array
            while l < r and self.valid_window(target_freq, window_freq):
                # shrink the window until it isn't valid

                # compute new length
                length = r - l + 1
                if length < min_length:
                    min_length = length
                    min_l = l
                    min_r = r
                
                # shrink window
                if s[l] in target_freq:
                    window_freq[s[l]] -= 1
                l += 1

                # print(f"Shrunk window : {s[l:r]}")
            
    
        return s[min_l:min_r]

