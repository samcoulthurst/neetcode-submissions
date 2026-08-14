class Solution:
    def reverseList(self, head):
        prev = None
        curr = head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev

    def reorderList(self, head):
        if not head or not head.next:
            return

        # Find the middle of the list
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Split the list into two halves
        second = slow.next
        slow.next = None

        # Reverse the second half
        second = self.reverseList(second)

        # Merge the two halves alternately
        first = head

        while second:
            first_next = first.next
            second_next = second.next

            first.next = second
            second.next = first_next

            first = first_next
            second = second_next