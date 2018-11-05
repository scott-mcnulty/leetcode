class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        if x < 0:
            return False
        
        s = str(x)
        start = 0
        end = len(s) - 1
        while start <= end:
            
            if s[start] != s[end]:
                return False
            
            start += 1
            end -= 1
            
        return True