# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if root == None:
            return result
        q = collections.deque()
        q.append(root)

        while(q):
            nodes = []
            for i in range(len(q)):
                node = q.popleft()
                nodes.append(node.val)
                if(node.left != None):
                    q.append(node.left)
                if(node.right != None):
                    q.append(node.right)
            result.insert(0, nodes)
        return result
