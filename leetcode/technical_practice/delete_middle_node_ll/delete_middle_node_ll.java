public ListNode deleteMiddle(ListNode head) {
        // Optimized would use two pointers with one moving twice as fast to find middle
        int count = 0;

        for (ListNode current = head; current != null; current = current.next) {
            count++;
        }

        double middle = Math.floor(count / 2);
        ListNode left = null;
        ListNode current = head;

        if (middle == 0) return null;

        for (int i = 0; i <= middle; i++) {
            
            if (i == middle) {
                left.next = current.next;

                break;
            }

            left = current;
            current = current.next;
        }

        return head;
    }
