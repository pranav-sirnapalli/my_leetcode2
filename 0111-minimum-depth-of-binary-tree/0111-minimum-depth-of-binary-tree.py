# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # If no root then no length
        if not root:
            return 0
        # as we are using BFS we will use queue
        q = collections.deque()
        q.append((root, 1))

        # loop it in current value
        while(q):
            node, depth = q.popleft()
            # If it has zero children we have reached maximum depth which means this is depth
            if not node.left and not node.right:
                return depth
            # left child present so add it to queue
            if(node.left):
                q.append((node.left, depth+1))
            # right child present so add it to queue
            if(node.right):
                q.append((node.right, depth+1))

            