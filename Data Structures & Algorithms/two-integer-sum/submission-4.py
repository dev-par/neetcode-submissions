class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # we want to look at the target - current number
        # if we don't have a pair, we add the current number to the hashmap as the key and 
        # its index as the value

        hashmap = {}
        for i, num in enumerate(nums):
            needed_num = target - num
            if needed_num in hashmap:
                return [hashmap[needed_num], i]
            hashmap[num] = i

        