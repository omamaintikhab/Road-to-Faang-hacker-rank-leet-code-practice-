# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return self.is_mirror(root.left, root.right)
    
    def is_mirror(self,left_node,right_node):
        # if left node and right node are not none then we will apply our condition recursively
        '''
        condition for symetric is root.left == root.right
        '''
        if left_node and right_node:
            return left_node.val == right_node.val and self.is_mirror(left_node.left,right_node.right) and self.is_mirror(left_node.right,right_node.left)
        
        return left_node == right_node