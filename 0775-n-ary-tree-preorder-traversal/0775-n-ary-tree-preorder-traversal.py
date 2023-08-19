"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        stack = [root] # Initialised the array to hold values
        result = [] # The final result is held here
        
        if not root:
            return []
        while(stack):
            tmp = stack.pop()   # Popping the last element pushed to stack
            result.append(tmp.val) # Add to result
            stack.extend(tmp.children[::-1])    # Followed by adding all children
        return result
        # children are added in reverse because in preorder we need to move from left to right
        # So by doing this we get the left most child on top of stack to be pushed into result next