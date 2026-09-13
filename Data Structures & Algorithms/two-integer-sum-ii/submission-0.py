class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # increasing nums list
        # return [index1, index2] that sum to target
        # they cannot be equal, both elements have to be distinct indicies 
        # always exactly one valid solution

        # only O(1) additional space
        # this makes me think we need to use a pointer approach

        # target = 9
        # 1, 3, 6, 9
        #    i  j

        # place a beginning and end pointer
        # if our sum is less than the target, move left pointer forward
        # if sum is more, move right pointer back

        i, j = 0, len(numbers) - 1

        while i < j:
            num_sum = numbers[i] + numbers[j]
            if num_sum > target:
                j -= 1
            elif num_sum < target:
                i += 1
            elif num_sum == target:
                return [i + 1,j + 1]
    