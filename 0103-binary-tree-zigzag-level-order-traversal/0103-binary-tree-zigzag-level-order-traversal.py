# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = [] # To hold the final traversal
        q = collections.deque([root] if root else []) # We need queue as we use FIFO in traversal

        while(q):
            qLength = len(q) # Holds length of queue
            level = []  # The order of traversal of current level
            for i in range(qLength):
                node = q.popleft()  # Popping the node which needs to be added at current level
                level.append(node.val)  # after adding value
                if(node.left):  # chk if left node exists and append if it does
                    q.append(node.left)
                if(node.right): # chk if right node exists and append if it does
                    q.append(node.right)
            level = reversed(level) if len(res)%2 else level    # Only reverse on even level as shown in question
            res.append(level)
        return res
                