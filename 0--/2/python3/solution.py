# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        # Collect the values of l1
        l1_values = ''
        while l1 is not None:
            l1_values = str(l1.val) + l1_values
            l1 = l1.next
        
        # Collect the values of l2
        l2_values = ''
        while l2 is not None:
            l2_values = str(l2.val) + l2_values
            l2 = l2.next
            
        # Add them together, reverse the result value
        reversed_sum = list(str(int(l1_values) + int(l2_values)))
        reversed_sum.reverse()
        reversed_sum = ''.join(reversed_sum)
        
        # Create new linked list of the reversed sum
        current_node = ListNode(reversed_sum[0])
        head = current_node
        for num in reversed_sum[1:]:
            new_node = ListNode(num)
            current_node.next = new_node
            current_node = new_node
            
        return head