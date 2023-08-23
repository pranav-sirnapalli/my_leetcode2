# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def generate(left, right):     # this is because sub-problem defined as range of no
            if(left > right):   # at some point both pointers overlap and better to return 
                return [None]       # empty array
            
            res = []
            for val in range(left, right+1): # any of these values can be root node
                for leftTree in generate(left, val-1): # This is to create left sub-tree, boundary should be upto val. This recusrsive call will build all left subtrees
                    for rightTree in generate(val+1, right): # This is to create right sub-tree, it should start from next value from val. This recursive call will build all right subtrees
                        root = TreeNode(val, leftTree, rightTree) # Current val is root and the left and right sub-trees are defined based on the looping
                        res.append(root)
            return res
        return generate(1, n)
                


