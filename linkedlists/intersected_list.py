# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        temp_headA, temp_headB = headA, headB
        if(temp_headA is None and temp_headB is None):
            return None
        temp_lst = []
        while(temp_headA.next):
            temp_lst.append(temp_headA)
            temp_headA = temp_headA.next

        while(temp_headB.next):
            if(temp_headB in temp_lst):
                return temp_headB.val
            temp_headB = temp_headB.next

        return None

        