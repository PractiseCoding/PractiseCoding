class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        if(x<0):
            isNumberNegative=1
        else:
            isNumberNegative=0
      
        x=abs(x)
        #result=int(str(x)[::-1])
        result=0
        while(x!=0):
            firstNumber=x%10
            result=firstNumber+(result*10)
            x=x/10

        print(result)
        
        
        if(result.bit_length()<32):
            if(isNumberNegative == 1):
                return -abs(result)
            else:
                return result
        else:
            return 0
        
