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

        # Create list of values from the linked lists
        all_values = list(map(lambda x: self.get_all_llist_values(x), non_empty_lls))
        all_values = list(itertools.chain.from_iterable(all_values))
        
        # Return a linked list from the sorted list of all values
        return self.create_llist_from_values_list(sorted(all_values))
    
    def get_non_empty_lls(self, lists):
        """
        Gives back a list of non-None node heads (ListNode) from the supplied
        list of head nodes
        """
        return [l for l in lists if l is not None]
        
    def create_llist_from_values_list(self, values_list):
        """
        Gives back a head node for a linked list that is created from
        the list of supplied values, values_list
        """
        if not values_list:
            return []

        head = ListNode(values_list[0])
        tail = head
        for value in values_list[1:]:
            new_node = ListNode(value)
            tail.next = new_node
            tail = tail.next

        return head
    
    def get_all_llist_values(self, llist):
        """
        Returns a list of values from a linked list
        """
        
        values = []
        while llist:
            values.append(llist.val)
            llist = llist.next
            
        return values