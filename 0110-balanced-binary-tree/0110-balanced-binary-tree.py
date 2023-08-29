# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):
            # If no root it means no tree hence height balanced
            if not root:
                return [True, 0]
            
            # In the below line we are trying to use the bottom-up heap
            # going to the left most bottom and right most bottom node so that we
            # can start chk height from bottom to top
            left, right = dfs(root.left), dfs(root.right)

            # chk at that particular level if it is balanced binary tree uptil this point
            # if left[0] or right[0] is False that means in prev step itself it has become
            # non height-balanced
            bool_val = (left[0] and right[0] and abs(left[1]-right[1])<=1)
            return [bool_val, 1 + max(left[1], right[1])]
        return dfs(root)[0]