###########Leetcode. 186###########
class Solution:
    def reverseWords(self, s: List[str]) -> None:
        s.reverse()
        print(s)
        
        index=0
        i=0
        n=len(s)
        
        while i < n:
            if s[i] == " ":
                s[index:i]=reversed(s[index:i])
                index=i+1
            i=i+1
        s[index: ] = reversed(s[index: ])
        
       
