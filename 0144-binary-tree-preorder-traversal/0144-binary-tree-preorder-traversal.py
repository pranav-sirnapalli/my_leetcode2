# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []    # To store the final traversal
        stack = []  # To store the rightmost node in every traversal
        curr = root # To make a pointer to the head node

        while(curr or stack):   
            if(curr):
                res.append(curr.val)    # Append the value as it is the parent
                stack.append(curr.right)    # Put right value in stack as this is what we need
                                            # to go to after we traverse the left end
                curr = curr.left        # Move to the left as we are trying to reach the end
            else:
                curr = stack.pop()  # popping to get the rightmost element which we can now get
                                    # our curr pointer to
        return res
        
        

