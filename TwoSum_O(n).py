class Solution(object):
    def twoSum(self, nums, target):
        dict={}
        result=[]
        for pointer1 in range(len(nums)):
            dict.update({pointer1:nums[pointer1]})
            firstNumber=nums[pointer1]
            secondNumber=target-firstNumber
            if(secondNumber in dict.values()):
                secondNumberIndex=nums.index(secondNumber)
                firstNumberIndex=pointer1
                if(pointer1!=secondNumberIndex):
                    result.append(secondNumberIndex)
                    result.append(firstNumberIndex)
        return result
