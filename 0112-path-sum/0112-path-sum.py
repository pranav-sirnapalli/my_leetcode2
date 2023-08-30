# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs(node, pathsum):
            # No root node so can't find sum
            if not node:
                return False
            
            # add sum at particular point
            pathsum += node.val

            # reached a leaf node so return at this point if true or false
            if(not node.left and not node.right):
                return pathsum == targetSum
            
            # if current node still has a left and right child move towards it
            return (dfs(node.left, pathsum) or dfs(node.right, pathsum))
        
        return dfs(root, 0)