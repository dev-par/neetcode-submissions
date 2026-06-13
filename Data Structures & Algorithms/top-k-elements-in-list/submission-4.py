from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = Counter(nums)


        # [ [], [], [] ]
        bucket = [[] for _ in range(len(nums) + 1)]


        for num, freq in freq_map.items():
            bucket[freq].append(num)
        
        res = []

        # bucket is 1 longer than nums, so we start at len(nums)
        for i in range(len(nums), -1, -1):
            
            for element in bucket[i]:

                if len(res) == k: 
                    return res

                res.append(element)
        
        return res
