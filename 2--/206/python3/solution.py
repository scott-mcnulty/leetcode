# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        # Empty given or linked list of length 1
        if (not head or head.next is None):
            return head
        
        # Start new list end with beginning of input list
        reversed_list = ListNode(head.val)
        head = head.next
        
        # # Add items to reversed list
        while head is not None:
            
            new_node = ListNode(head.val)
            new_node.next = reversed_list
            reversed_list = new_node
            head = head.next
            
        return reversed_list

        # Recursive implementation
        # reversed_list = ListNode(head.val)
        # head = head.next
        # return self._reverse_list_helper(head, reversed_list)



    def _reverse_list_helper(self, head, reversed_list):
        """
        Recursive implementation
        """

        if (head.next is None):

            head.next = reversed_list
            return head

        else:

            new_node = ListNode(head.val)
            new_node.next = reversed_list
            reversed_list = new_node
            return self._reverse_list_helper(head.next, reversed_list)