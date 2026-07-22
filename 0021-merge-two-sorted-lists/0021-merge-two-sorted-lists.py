# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(
        self,
        list1: Optional[ListNode],
        list2: Optional[ListNode]
    ) -> Optional[ListNode]:

        dummy = ListNode(0)
        self.cur = dummy

        def rec(n1, n2):
            if not n1 or not n2:
                self.cur.next = n1 or n2
                return

            if n1.val <= n2.val:
                self.cur.next = n1
                self.cur = self.cur.next
                rec(n1.next, n2)
            else:
                self.cur.next = n2
                self.cur = self.cur.next
                rec(n1, n2.next)

        rec(list1, list2)

        return dummy.next