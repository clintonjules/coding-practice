# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def get_num(ll):
            current = ll

            num = 0
            count = 0
            while current != None:
                num += (10**count) * current.val

                count += 1
                current = current.next

            return num


        ll_sum = list(str(get_num(l1) + get_num(l2))[::-1])
        
        head = ListNode(val = int(ll_sum[0]), next = None)
        out = head
        for n in ll_sum[1:]:
            out.next = ListNode(val = int(n), next = None)
            out = out.next

        return head
