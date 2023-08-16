# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = [] # For all the values
        stack = [] # To store till we reach extreme left node
        cur = root # start point
        while cur or stack: 
            while cur:
                stack.append(cur)  # appending values
                cur = cur.left  
            cur = stack.pop() # popping as we reach extremem left
            res.append(cur.val) # adding it to result
            cur = cur.right # move to right
        return res