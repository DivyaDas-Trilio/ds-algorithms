# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution: # This is modified version of problem
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp_head = head
        temp_var = None
        try:
            if(temp_head.next):
                while(temp_head.next.next):
                    temp_var = temp_head.val
                    if(temp_head.next.val > temp_var):
                        temp_var = temp_head.next.val
                    else:
                        temp_head.next = temp_head.next.next
                        temp_head.next.next = None
                    temp_head = temp_head.next
                if(head.val == temp_head.next.val):
                    head.next = None 

        except AttributeError as ae:
            return head  
        
            