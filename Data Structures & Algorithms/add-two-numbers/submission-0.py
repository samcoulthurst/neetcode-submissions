# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = node = ListNode()
        carry = 0
        while list1 or list2 or carry:

            v1 = list1.val if list1 else 0
            v2 = list2.val if list2 else 0

            value = v1 + v2 + carry
            remainder = value % 10
            carry = value // 10
            node.next = ListNode(remainder)

            node = node.next
            list1 = list1.next if list1 else None
            list2 = list2.next if list2 else None

        return dummy.next

        