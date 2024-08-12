# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head: return head

        while head.val == val:
            if head.next: head = head.next
            else: return None

        curr = head

        while curr:
            if curr.next:
                if curr.next.val == val:
                    if curr.next.next: 
                        curr.next = curr.next.next
                    else:
                        curr.next = None
                        return head
                else: 
                    curr=curr.next
            else:
                curr.next = None
                return head
