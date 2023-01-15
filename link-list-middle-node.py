# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        inc = 0
        temp = head
        head2 = head
        step = 0
        while temp is not None:
            inc = inc + 1
            temp =temp.next

        mod = inc%2
        print("inc",inc)
        print("mod",mod)
        if mod == 0:
            step = inc//2
            
        elif mod == 1:
            step = inc // 2
            print("step befor add",step)
            

        i = 0
        print(step)
        if head2.next is not None:
            
            while i<step:
                print(head.val)
                head2 = head2.next
                i+=1
            return head2
        else:
            return head