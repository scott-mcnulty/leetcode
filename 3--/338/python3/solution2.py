class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        
        num_1s = []
        for n in range(num + 1):
            
            # Convert num to binary string
            binary_string = self.decimal_to_base_b(n, 2, '')

            # Count the nums
            num_1s.append(binary_string.count('1'))

        return num_1s
    
    def decimal_to_base_b(self, num, b, result):
        '''
        Takes a decimal num and a base b numbering system
        to convert to. Gives base the new value with base base
        '''

        if num == 0:
            return result

        else:
            result = str(int(num) % b) + result
            num = int(num) // b
            return self.decimal_to_base_b(num, b, result)