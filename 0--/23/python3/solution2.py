"""
This solution works but not in the alloted time on leetcode.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        # Make a list of the lists that are not empty
        non_empty_lls = self.get_non_empty_lls(lists)

        # If the all empty return []
        if not non_empty_lls:
            return []
        
        # Find the lowest element to start the new list
        smallest_node, smallest_node_index = self.get_smalles_node_of_lists(non_empty_lls)
        
        # Start the new list and advance the list that was the smallest
        head = ListNode(smallest_node.val)
        tail = head
        non_empty_lls[smallest_node_index] = non_empty_lls[smallest_node_index].next
        
        # Reset the non_empty_lls list in case the list we advanced had 1 node
        non_empty_lls = self.get_non_empty_lls(non_empty_lls)
        
        # Loop that continues if there are non empty lists
        while non_empty_lls:
        
            # Find the smallest head element of all the lists
            smallest_node, smallest_node_index = self.get_smalles_node_of_lists(non_empty_lls)
            
            # Add it to the new list
            tail.next = ListNode(smallest_node.val)
            
            # Advance the new list tail and list the element was pulled from
            tail = tail.next
            non_empty_lls[smallest_node_index] = non_empty_lls[smallest_node_index].next
            
            # Get the list of non empty lists
            non_empty_lls = self.get_non_empty_lls(non_empty_lls)
        
        return head
    
    def get_non_empty_lls(self, lists):
        """
        Gives back a list of non-None node heads (ListNode) from the supplied
        list of head nodes
        """
        return [l for l in lists if l is not None]
        
    def get_smalles_node_of_lists(self, llists):
        """
        Gets the smallest node value and index in the list of
        supplied node heads.
        
        returns (ListNode, index) where index is the index of ListNode in llists
        """
        smallest_node = None
        smallest_node_index = -1
        for ll_index, ll in enumerate(llists):
            
            try:
                
                if (ll.val < smallest_node.val):
                    smallest_node = ll
                    smallest_node_index = ll_index
                    
            # We haven't set the smallest yet
            except AttributeError:
                smallest_node = ll
                smallest_node_index = ll_index
                
        return (smallest_node, smallest_node_index)