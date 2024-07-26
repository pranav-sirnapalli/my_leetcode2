# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(root, ans):
            if(root.left is None and root.right is None):
                ans.append(root.val)
                return ans
            else:
                if root.left:
                    dfs(root.left, ans)
                if root.right:
                    dfs(root.right, ans)

        ans1 = []
        ans2 = []
        dfs(root1, ans1)
        dfs(root2, ans2)

        if(ans1 == ans2):
            return True
        return False
        