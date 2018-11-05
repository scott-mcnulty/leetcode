class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        
        num_1s = []
        for n in range(num + 1):

            # Convert num to binary string
            # This is faster than in solution 2. Leetcode marks the runtime at 140 ms
            # here compared to 1400+ ms
            binary_string = '{0:b}'.format(n)

            # Count the nums
            num_1s.append(binary_string.count('1'))

        return num_1s