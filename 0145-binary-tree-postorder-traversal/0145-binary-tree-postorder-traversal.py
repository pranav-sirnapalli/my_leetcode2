# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [root]  # This will hold all the nodes we visit, we are initialising it as root will be present in it at the begining
        visit = [False] # As we add the value to result only when it has been visited second time this will hold whether it has been visited or not, as root is not yet visited intialised to False
        result = [] # Final traversal

        while stack:
            cur, v = stack.pop(), visit.pop() # popping last element and whether we are visting second time
            if cur:
                if v:
                    result.append(cur.val)  # appending as v had value True
                else:
                    stack.append(cur)   # appending to stack as it had false
                    visit.append(True)  # Now can be initialised to true
                    stack.append(cur.right)  # appending right child as that is next after left
                    visit.append(False) # false not been visited yet
                    stack.append(cur.left) # appending left child as that is before right
                    visit.append(False) # false not been visited yet
        return result   # final result



