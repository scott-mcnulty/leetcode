# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        # Check inputs
        # Both empty
        if not l1 and not l2:
            return None

        # l2 empty but not l1
        elif l1 and not l2:
            return l1

        # l1 empty but not l2
        elif not l1 and l2:
            return l2

        # See which value is lowest to begin the new merged list
        else:
            
            # l1 less than l2
            if (l1.val < l2.val):
                head = ListNode(l1.val)
                l1 = l1.next
              
            # l2 larger than l1
            else:
                head = ListNode(l2.val)
                l2 = l2.next
        
        # Keep adding elements to the merged list
        tail = head
        while l1 and l2:
            
            # l1 less than l2
            if (l1.val < l2.val):
                new_node = ListNode(l1.val)
                tail.next = new_node
                l1 = l1.next
              
            # l2 larger than l1
            else:
                new_node = ListNode(l2.val)
                tail.next = new_node
                l2 = l2.next
                
            tail = tail.next
        
        # Check for any dangling elements to add
        # l2 empty but not l1
        if l1 and not l2:
            tail.next = l1
                
        # l1 empty but not l2
        elif not l1 and l2:
            tail.next = l2

        return head