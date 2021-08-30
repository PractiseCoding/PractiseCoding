class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        S=list(s)
        i=0
        j=len(S)-1
        while i<j:
            if S[i].isalpha() and S[j].isalpha():
                S[i],S[j]=S[j],S[i]
                i=i+1
                j=j-1
            if not S[i].isalpha():
                i=i+1
            if not S[j].isalpha():
                j=j-1
        return "".join(S)
