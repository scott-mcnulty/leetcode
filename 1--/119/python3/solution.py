class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        
        from math import factorial
        
        # https://en.wikipedia.org/wiki/Pascal%27s_triangle
        # Make our row of 'n choose k' values
        numerator = factorial(rowIndex)
        row = []
        for k in range(rowIndex + 1):
            
            denominator = factorial(k) * factorial(rowIndex - k)
            row.append(int(numerator / denominator))
        
        return row