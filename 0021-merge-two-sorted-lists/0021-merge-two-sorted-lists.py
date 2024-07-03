# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
       
        # Creating the default node(0)
        mergerd_list = ListNode()
        curr = mergerd_list

        # Merging the lists
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
            
         # Attaching the remaining nodes
        if list1:
            curr.next = list1
        else:            
            curr.next = list2

        # Return the merged list
        return mergerd_list.next