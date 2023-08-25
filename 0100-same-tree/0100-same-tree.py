# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        # This shows that root doesen't match so return false
        if ((not p or not q) or (p.val != q.val)):
            return False
        
        # chk every child left node and right node using below recusrion
        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))