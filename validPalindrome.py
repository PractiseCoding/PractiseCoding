class Solution(object):
    def isPalindrome(self, s):
        actual_word = ""
        for i in s:
            if i.isalnum():
                actual_word += i
        reversed_word=actual_word[::-1]
        
        if (lower(actual_word) == lower(reversed_word)):
            return True
        else:
            return False
                
