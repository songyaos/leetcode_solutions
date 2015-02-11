# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrderBottom(self, root):
        next_level = []
        current_level =[root]
        result = []
        
        while current_level:
            temp = []
            for node in current_level:
                if node:
                    temp.append(node.val)
                    if node.left:
                        next_level.append(node.left)
                    if node.right:
                        next_level.append(node.right)
            if temp:
                result.append(temp)
            current_level=  next_level
            next_level=[]
            
        temp= [result[len(result)-i-1] for i in range(len(result))]
        return temp
        