class Solution:
    def length(self, head):
        curr = head
        l = 0
        while curr:
            l += 1
            curr = curr.next
        return l

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = self.length(head)
        if l == n:
            return head.next
        curr = head
        for i in range(l-n-1):
            curr = curr.next
        curr.next = curr.next.next
        return head