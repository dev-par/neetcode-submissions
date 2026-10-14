# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # linked list
        # 0 -> 1 -> 2 -> 3
        # null -> 0 -> 1 -> 2 -> 3 -> null

        # initalize prev to head
        # start at head.next
        # store the next node as temp
        # make node.next = prev
        # 
        node = head
        prev = None
        while node:
            temp = node.next
            node.next = prev
            prev = node
            node = temp
        
        return prev
        

