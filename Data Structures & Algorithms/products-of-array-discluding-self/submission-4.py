class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # return the product of each number except itself


        # naieve solution is to iterate through the array, skip the current index, and multiply all others
        """
        result = []
        for i in range(len(nums)):
            curr = 1
            for j in range(0, len(nums)):
                if i != j:
                    curr *= nums[j]
            result.append(curr)
        
        return result
        """

        # multiply all the numbers to get a total 
        # iterate through the array and divide the total by each individual number
        # if there are more than 2 zeros in the array, the entire result will be zeros
        # if there is one zero, only that position will have the total product 
        """
        total = 1
        zeros = 0
        for num in nums:
            if num:
                total *= num
            else:
                zeros += 1
        
        result = []
        if zeros >= 2:
            return [0] * len(nums)
        if zeros == 1:
            for num in nums: 
                if num == 0:
                    result.append(total)
                else:
                    result.append(0)
        else:
            for num in nums: 
                result.append(total // num)

        return result
        """
        # [1,1,2,8]
        # near optimal - create prefix and postfix arrays
        # multiply the product of all values before and after 
        pre = [1] * len(nums)
        post = [1] * len(nums)
        result = [1] * len(nums)
        for i in range(1, len(nums)):
            # multiply by all the previous prefixes [i-1] of prefix array
            pre[i] = pre[i-1] * nums[i-1]
        for i in range(len(nums) - 2, -1, -1):
            post[i] = post[i + 1] * nums[i+1]
        
        for i in range(len(nums)):
            result[i] = pre[i] * post[i]

        return result

