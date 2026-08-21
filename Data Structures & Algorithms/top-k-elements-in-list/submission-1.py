from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # sort by frequency
        # create an array where the index = frequency
        # this is fine because frequency <= len(nums)
        # iterate backwards over the array until your output array len == k

        # create an array of len frequency
        # each index has to be a list because two numbers can have the same frequency
        result = []
        # why do we need the + 1 here? 
        bucket_sort = [[] for i in range(len(nums) + 1)]
        freq_count = Counter(nums)
        for num, freq in freq_count.items():
            bucket_sort[freq].append(num)
        
        for i in range(len(nums), -1, -1):
            for item in bucket_sort[i]:
                result.append(item)
                if len(result) == k:
                    return result
