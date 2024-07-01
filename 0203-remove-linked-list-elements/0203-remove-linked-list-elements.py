# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head == None:
            return head

       # if starting nodes are equal to val
        while head != None and head.val == val:
            head = head.next
        
        if head ==  None:
            return head

        # deleting from center/end 
        
        curr = head
        while curr.next:
            if curr.next.val != val:
                curr =  curr.next                
            else:
                curr.next = curr.next.next

        return head        


            



            
                


