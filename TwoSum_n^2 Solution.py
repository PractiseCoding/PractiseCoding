class Solution(object):
    def twoSum(self, nums, target):
        sum=0
        result=[]
        for pointer1 in range(len(nums)):
            for pointer2 in range(pointer1+1,len(nums)):
                sum=nums[pointer1]+nums[pointer2]    
                if (sum == target):
                    result.append(pointer1)
                    result.append(pointer2)
        return result
