class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if not s:
            return 0
        
        # Iterate over the characters to use that character as
        # the start of a stubstring
        max_length = -1
        for index, character in enumerate(s):
            
            tmp_substring = character
            
            # Continue adding characters as long as unique
            tmp_index = index + 1
            while tmp_index < len(s) and s[tmp_index] not in tmp_substring:
                tmp_substring += s[tmp_index]
                tmp_index += 1
                
            # Compare the substring length to the max we've found
            if len(tmp_substring) > max_length:
                max_length = len(tmp_substring)
    
    
        return max_length
            


sol = Solution()
a = "abcabcbb"
sol.lengthOfLongestSubstring(a)