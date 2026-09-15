class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # what is binary search
        # when doing binary search, we start at the middle position of a sorted array
        # and check if that value is higher, lower, or equal to the desired val
        
        # if the val is higher, the new array becomes the left portion (not including the current middle)
        # if lower, right portion
        # repeat until we get the desired val or there's no more values?

        # two pointers to track the start and end of the array

        l, r = 0, len(nums) - 1
        while l <= r:
            # calculate the midpoint
            # take half the relative distance and add the lower
            mid = l + ((r - l) // 2)
            
            # 3 cases
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
        return -1
    