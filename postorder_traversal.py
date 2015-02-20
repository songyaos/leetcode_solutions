# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        node =root
        result =[]
        self.postorder(node, result)
        return result
        
    def postorder(self, node, result):
        if node:
            self.postorder(node.left,result)
            self.postorder(node.right,result)
            result.append(node.val)