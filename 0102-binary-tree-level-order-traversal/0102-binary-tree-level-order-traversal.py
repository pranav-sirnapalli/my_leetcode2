# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = [] # To hold the result

        q = collections.deque() # We are using a queue because we need to pop the first element which will then be placed in list res and then left and right child of that can be placed back here
        q.append(root) # Appending the first value to queue

        while(q):
            qLength = len(q) # Consider the length of the queue as we need to pop till end
            level = [] # To add each level
            for i in range(qLength):    # In that level length
                node = q.popleft()  # pop the first element in queue as it is next node
                if(node):   # assuming node exists
                    level.append(node.val)  # add that node to level
                    q.append(node.left) # append left child node to queue
                    q.append(node.right)    # append right child node to queue
            if(level):  # if level is not null
                res.append(level)   # add it to final result
        return res
