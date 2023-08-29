# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        # To find the length of the linked list
        # we know mid of linked list will be root node
        n = 0
        curr = head
        while(curr):
            curr = curr.next
            n += 1
        
        self.head = head

        def help(st, end):
            # Left node overlapped right node need to break out
            if(st>end):
                return None
            # To always find mid
            mid = (st + end) // 2
            # we calculate for left node here as it will change in the next steps
            left = help(st, mid-1)
            # Designing the root node
            root = TreeNode(self.head.val)
            self.head = self.head.next
            # Now assign left as the st will change we move one node front
            root.left = left
            # Now assign right tree as usual similar to last question
            root.right = help(mid+1, end)
            return root
        return help(0, n-1)
        