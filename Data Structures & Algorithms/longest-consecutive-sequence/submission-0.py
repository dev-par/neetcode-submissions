class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # order in the original array doesn't matter
        # set membership is an idea
        # we could sort and count sequences
        
        # naieve way is to use set membership for each number to check for n + 1
        # we need to realize that we only want to start counting when we find the 
        # beginning of a sequence

        # if n - 1 isn't in the list, we have the beginning number of a possible sequence
        # check forward from there

        nums_set = set(nums)
        longest_sequence = 0

        for n in nums:
            if n - 1 in nums_set:
                continue

            # if start of sequence, start counting
            sequence = 0
            while n in nums_set:
                n += 1
                sequence += 1

            longest_sequence = max(sequence, longest_sequence)
        
        return longest_sequence