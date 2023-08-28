# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # It is not possible to build tree if we had only one of the traversal
        if not preorder or not inorder:
            return None
        
        # we know the first node in preorder is the root and so we can add the root node
        root = TreeNode(preorder[0])
        # the root node will be the middle in inorder list, so find the mid using that
        mid = inorder.index(preorder[0])
        #Find the left subtree by recursion as everything on left of root will be underthemid 
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        #Find the right subtree by recursion as everything on right of root will be abovethemid
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return root