# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return head

        # initialize fast slow pointers
        slow_p = head
        fast_p = head

        while fast_p and fast_p.next:
            slow_p = slow_p.next
            fast_p = fast_p.next.next

        # reverse list from slow_p/second half
        temp = slow_p
        nextt = None

        while temp:
            next_node = temp.next
            temp.next = nextt
            nextt = temp
            temp = next_node
            

        # comparing both half reversed & starting head
        left_p = head
        right_p = nextt

        while right_p:
            if left_p.val != right_p.val:
                return False
           
            left_p = left_p.next
            right_p = right_p.next
        return True  