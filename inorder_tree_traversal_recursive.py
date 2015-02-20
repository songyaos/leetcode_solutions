# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        node =root
        result =[]
        self.inorder(node, result)
        return result
        
    def inorder(self, node, result):
        if node:
            self.inorder(node.left,result)
            result.append(node.val)
            self.inorder(node.right,result)