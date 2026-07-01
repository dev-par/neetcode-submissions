from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = Counter(nums)

        # now we have all the frequencies

        freq = [[] for _ in range(len(nums) + 1)]
        for num, f in freq_map.items():
            freq[f].append(num)
        
        res = []
        for i in range(len(freq) - 1, -1, -1):
            print(i)
            if freq[i] != []:
                for item in freq[i]:
                    res.append(item)
                    if len(res) == k:
                        return res