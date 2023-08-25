# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # This is to hold the final tree
        self.tmp = []

        # Traverse through the whole list currently
        def dfs(node):
            if not node:
                return []
            dfs(node.left)
            self.tmp.append(node)
            dfs(node.right)
        dfs(root)

        # By sorting we are making the list of values
        srt = sorted(n.val for n in self.tmp)

        # Change the values according to what they are now in the tree
        for i in range(len(srt)):
            self.tmp[i].val = srt[i]
        return self.tmp
