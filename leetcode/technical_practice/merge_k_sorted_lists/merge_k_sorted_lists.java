public ListNode mergeKLists(ListNode[] lists) {
        // Check if lists is not empty
        if (lists == null || lists.length == 0) return null;

        PriorityQueue<ListNode> minHeap = new PriorityQueue<>((n1, n2) -> n1.val - n2.val);
        
        for (ListNode list_head: lists) {
           if (list_head != null) minHeap.add(list_head);
        }
        
        // Break it down: only need to look at the head values since lists are sorted
        // Choose lowest from the values


        // Dummy head for the merged list
        ListNode head = new ListNode(0);
        ListNode current = head;

        // Construct the merged list
        while (!minHeap.isEmpty()) {
            ListNode minNode = minHeap.poll();

            current.next = minNode;
            current = current.next;

            // If there's more in the list, add the next node to the min-heap
            if (minNode.next != null)
                minHeap.add(minNode.next);
        }

        return head.next;
    }
