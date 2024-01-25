def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    tortoise = head
    hare = head

    for _ in range(n):
        hare = hare.next

    if not hare:
        return head.next

    while hare.next != None:
        hare = hare.next
        tortoise = tortoise.next

    tortoise.next = tortoise.next.next

    return head
