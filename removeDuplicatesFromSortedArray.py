class Solution(object):
    def removeDuplicates(self, nums):
        
        if nums == None:
            return 0
        else:
            i=0
            for j in range(len(nums)):
                if nums[i] != nums[j]:
                    i=i+1
                    nums[i]=nums[j]
            return i+1
