# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:#notice pythonic condition style
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        stack = []
        result = []
        node = root
        while node or stack:
            if node:
                stack.append(node)
                node= node.left
            else:
                node = stack.pop()
                result.append(node.val)
                node = node.right
        return result