from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)

        # we now have all the frequencies
        # create an array of length len(nums) - 1
        # iterate over the counter and place each number in the index that 
        # cooresponds to it's frequency

        # loop backwards over the array and return once you've found k numbers

        freq_array = [[] for _ in range(len(nums) + 1)]
        for num, frequency in freq.items():
            # can have two numbers with the same frequency
            freq_array[frequency].append(num)
        
        res = []
        for i in range(len(nums), -1, -1):
            for num in freq_array[i]:
                res.append(num)
                if len(res) == k:
                    return res
