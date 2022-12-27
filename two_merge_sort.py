# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merg = ListNode()
        head = merg
        if list1 is not None and list2 is None:
            while list1 is not None:
                head.next = list1
                list1 = list1.next
                head = head.next
            return merg.next
        elif list2 is not None and list1 is None:
            while list2 is not None:
                head.next = list2
                list2 = list2.next
                head = head.next
            return merg.next
        elif list1 is not None and list2 is not None:
            while list1 is not None and list2 is not None:
                if list1.val<list2.val:
                    head.next = list1
                    list1= list1.next
                else:
                    head.next = list2
                    list2 = list2.next
                head = head.next
        while list1 is not None :
                head.next = list1
                list1 = list1.next
                head = head.next
        while list2 is not None:
                head.next = list2
                list2 = list2.next
                head = head.next
        
        return merg.next