# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        #inorder traversal
        node=root
        if not node:
            return False
        stack=[(node, sum)]
        while stack:
            node, res_sum = stack.pop()
            if not node.left and not node.right and node.val == res_sum:
                return True
            if node.left:
                stack.append((node.left, res_sum - node.val))
            if node.right:
                stack.append((node.right,res_sum - node.val))
        
        return False
        