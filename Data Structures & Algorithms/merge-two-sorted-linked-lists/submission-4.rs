impl Solution {
    pub fn append_ln(mut head: Option<Box<ListNode>>, new_val: i32) -> Option<Box<ListNode>> {
        let new_node = Box::new(ListNode::new(new_val));

        if head.is_none() {
            return Some(new_node);
        }

        let mut current = &mut head;
        // FIX: Removed 'ref mut' to comply with Rust's implicit binding modes
        while let Some(node) = current {
            if node.next.is_none() {
                node.next = Some(new_node);
                break;
            }
            current = &mut node.next;
        }

        head
    }

    pub fn merge_two_lists(mut list1: Option<Box<ListNode>>, mut list2: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut dummy = ListNode::new(0);
        let mut current = &mut dummy.next;

        while let (Some(l1), Some(l2)) = (&list1, &list2) {
            if l1.val <= l2.val {
                let mut next = list1.take().unwrap();
                list1 = next.next.take();
                *current = Some(next);
            } else {
                let mut next = list2.take().unwrap();
                list2 = next.next.take();
                *current = Some(next);
            }

            // FIX: Removed 'ref mut' here as well
            if let Some(node) = current {
                current = &mut node.next;
            }
        } // FIX: Closed the while loop block here

        // FIX: Moved cleanup and return statement outside of the while loop
        *current = if list1.is_some() { list1 } else { list2 };

        dummy.next
    }
}
