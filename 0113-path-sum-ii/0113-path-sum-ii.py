# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        self.result = []

        def dfs(node, path, sum):
            sum += node.val
            tmp = path + [node.val]
            if(node.left):
                dfs(node.left, tmp, sum)
            
            if(node.right):
                dfs(node.right, tmp, sum)
            
            if(not node.left and not node.right and sum == targetSum):
                self.result.append(tmp)          
        
        if not root:
            return []

        dfs(root, [], 0)
        return self.result