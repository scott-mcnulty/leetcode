class Solution:
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        
        # Iterate over the cookie sizes to see who can be satisfied
        satisfied_people = []
        for cookie in s:
            
            # Can only give a cookie away to one person
            if cookie in g and cookie not in satisfied_people:
                satisfied_people.append(cookie)
                
        return len(satisfied_people)