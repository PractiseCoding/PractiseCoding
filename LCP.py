class Solution(object):
    def longestCommonPrefix(self, strs):
        
        if(len(strs)==0):
            return ""
        elif(len(strs)==1):
            return strs[0]
        else:
        
            print(strs)
            strs.sort()
            print(strs)
            commonPrefix=""
            for i in range(len(strs[0])):
                if(strs[0][i]==strs[-1][i]):
                    commonPrefix+=strs[0][i]
                else:
                    break
            return commonPrefix
