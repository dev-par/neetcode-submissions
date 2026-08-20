class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # two for loops and check all possible combinations
        # how can we make this O(n)
        # we want an O(1) check to see if a number we've previously seen is our desired number
        # store previous numbers in a hashmap with number : index format
        # calculate the needed number for our current and check the map
        # if not in the map, add and iterate

        num_map = {}
        for i, num in enumerate(nums):
            needed = target - num
            if needed in num_map:
                return [num_map[needed], i]
            num_map[num] = i