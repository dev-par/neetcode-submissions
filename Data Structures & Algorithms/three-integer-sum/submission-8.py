class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # return the triplets where nums[i] + j + k == 0

        # nums is not sorted
        # sort it and run two sum ii for each number

        # we can sort it cause we're not returning the index

        nums.sort()

        res = []

        for index, num in enumerate(nums):
            if index == len(nums):
                return res
            if index > 0 and nums[index] == nums[index - 1]:
                continue

            i, j = index + 1, len(nums) - 1
            target = -nums[index]
            while i < j:
                # since the array is sorted, if we have a duplicate left value we skip
                if nums[i] + nums[j] == target:
                    res.append([nums[index], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i-1]:
                        i += 1
                elif nums[i] + nums[j] > target:
                    j -= 1
                elif nums[i] + nums[j] < target:
                    i += 1
        return res
    