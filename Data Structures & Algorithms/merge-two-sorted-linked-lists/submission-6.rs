// Definition for singly-linked list.
// #[derive(PartialEq, Eq, Clone, Debug)]
// pub struct ListNode {
//     pub val: i32,
//     pub next: Option<Box<ListNode>>,
// }
//
// impl ListNode {
//     #[inline]
//     pub fn new(val: i32) -> Self {
//         ListNode { next: None, val }
//     }
// }

impl Solution {
    pub fn append_ln(mut head: Option<Box<ListNode>>, new_val: i32) -> Option<Box<ListNode>> {
        let new_node = Box::new(ListNode::new(new_val));

        if head.is_none() {
            return Some(new_node);
        }

        let mut current = &mut head;
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

            if let Some(node) = current {
                current = &mut node.next;
            }
        }

        *current = if list1.is_some() { list1 } else { list2 };

        dummy.next
    }
}
