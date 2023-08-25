# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(left, right):
            # if there are no left and right child at exact point then it is symmetric
            if(not left and not right):
                return True
            # if left child does not exist but right does or the other way around then
            # it is not symmetric
            if(not left or not right):
                return False

            # Go through every val and if it is equal then chk the left and right children
            return (left.val == right.val and dfs(left.left, right.right) and dfs(left.right, right.left))

        return dfs(root.left, root.right)