# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # start at the head of both lists

        # create a dummy node
        dummy = ListNode()
        node = ListNode()
        node.next = dummy

        while list1 and list2:
            list1Val = list1.val
            list2Val = list2.val

            if list1Val <= list2Val:
                dummy.next = list1
                list1 = list1.next
            else:
                dummy.next = list2
                list2 = list2.next
            
            dummy = dummy.next

        if list1:
            dummy.next = list1
        else:
            dummy.next = list2

        return node.next.next