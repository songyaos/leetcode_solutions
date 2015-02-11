# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        node = root
        if not node:
            return 0
        
        current_level = [node]
        next_level = []
        height = 0
        while current_level:
            height = height + 1
            for item in current_level:
                if not item.left and not item.right:
                    return height
                if item.left:
                    next_level.append(item.left)
                if item.right:
                    next_level.append(item.right)
            current_level = next_level
            next_level = []
            
        return height
                
                
                
            