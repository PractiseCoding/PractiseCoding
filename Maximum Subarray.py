class Solution(object):
    def maxSubArray(self, nums):
        maximum=nums[0]
        if(len(nums)==1):
            return nums[0]
        else:
            for i in range(1, len(nums)):
                nums[i]=max(nums[i], nums[i]+nums[i-1])
                maximum=max(nums[i],maximum)
            return  maximum
