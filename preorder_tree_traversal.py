# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        node =root
        result =[]
        self.preorder(node, result)
        return result
        
    def preorder(self, node, result):
        if node:
            result.append(node.val)
            self.preorder(node.left,result)
            self.preorder(node.right,result)
    
            
        