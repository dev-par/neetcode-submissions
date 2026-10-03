class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # setup pointers at the start and end of the array
        # calculate the area and save is as best area
        # if we're moving in, we're reducing the base, so the only way to get a larger area 
        # is to find a higher bar
        # we move the index representing the shorter bar 

        best_area = 0
        l, r = 0, len(heights) - 1
        while l < r:
            left_height = heights[l]
            right_height = heights[r]
            area = (r - l) * min(left_height, right_height)
            best_area = max(area, best_area)
            if left_height > right_height:
                r -= 1
            else:
                l += 1
        
        return best_area