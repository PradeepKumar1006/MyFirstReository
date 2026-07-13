class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head

        # Move prev to the node before 'left'
        prev = dummy
        for _ in range(left - 1):
            prev = prev.next

        # Reverse the sublist
        curr = prev.next
        prev_node = None

        for _ in range(right - left + 1):
            nxt = curr.next
            curr.next = prev_node
            prev_node = curr
            curr = nxt

        # Connect the reversed part back
        tail = prev.next          # Original left node (now becomes tail)
        prev.next = prev_node     # New head of reversed sublist
        tail.next = curr          # Connect tail to remaining list

        return dummy.next