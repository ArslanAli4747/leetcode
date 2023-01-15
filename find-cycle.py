# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # dic = {}
        # temp = head
        # pos = 0
        # if temp is None:
        #     return None
        # while temp.next is not None:
        #     if temp.next in dic.values() :
        #         break
        #     else:
        #         dic[str(temp.val)] = temp
        #     pos+=1
        #     temp = temp.next
        # print(pos)
        # print(dic)
        # if pos == 0:
        #     return None
        # else:
        #     return temp.next
            # Edge case: empty list or a list with only one element
        if not head or not head.next:
            return None
        
        # Initialize the pointers
        tortoise = head
        hare = head
        
        # Step 1: Find if there's a cycle
        while hare and hare.next:
            tortoise = tortoise.next
            hare = hare.next.next
            
            if tortoise == hare:
                break
        else:
            return None
        
        # Step 2: Find the start of the cycle
        tortoise = head
        while tortoise != hare:
            tortoise = tortoise.next
            hare = hare.next
        
        return hare

            
            
                