# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        if (not root):
            return []

        row_values = []
        row_values = self.build_values_list([root], row_values)
        
        # Get the max value from each row
        result = [max(row) for row in row_values]
            
        return result
        
    def build_values_list(self, nodes, collected_values_list):
        """
        Builds a list of values for the given list of nodes.
        Meant to traverse a tree and collect all the values as a list of lists
        where each list is a row:

        1   [       [a], 
        2           [a, d], 
        3           [d, y, c, b], ...
            ]
        """
        
        # No more node values to collect
        if (not nodes):
            return collected_values_list
        
        # Collect node values
        else:
            
            row_values = []
            node_children = []
            for node in nodes:
                row_values.append(node.val)
                node_children += self.get_child_list(node)

            collected_values_list += [row_values]
            return self.build_values_list(node_children, collected_values_list)
        
        
    def get_child_list(self, node):
        """
        Returns a list of child nodes to the
        given node.
        """
        children = []
        if (node.left):
            children += [node.left]
            
        if (node.right):
            children += [node.right]
            
        return children