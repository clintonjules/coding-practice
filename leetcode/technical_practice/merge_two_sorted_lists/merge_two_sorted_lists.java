public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
    if (list1 == null && list2 == null) return null;

    ListNode[] lists = new ListNode[]{list1, list2};

    PriorityQueue<ListNode> minHeap = new PriorityQueue<>((n1, n2) -> n1.val - n2.val);

    for (ListNode list_head: lists) 
        if (list_head != null) minHeap.add(list_head);

    ListNode head = new ListNode(0);
    ListNode current = head;

    while (!minHeap.isEmpty()) {
        ListNode min = minHeap.poll();

        current.next = min;
        current = current.next;

        if (min.next != null)
            minHeap.add(min.next);
    }

    return head.next;
}
