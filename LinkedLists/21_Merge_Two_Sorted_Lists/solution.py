# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    # Solution 1
    def mergeTwoLists(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:

        final = ListNode()
        current = final

        while l1 != None and l2 != None:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next

            current = current.next

        if l1 != None:
            current.next = l1

        if l2 != None:
            current.next = l2

        return final.next

    # Solution 2
    def mergeTwoLists(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        while l1 != None or l2 != None:
            v1, v2 = 101, 101

            if l1 != None:
                v1 = l1.val
            if l2 != None:
                v2 = l2.val

            if v1 >= v2:
                val = v2
                l2 = l2.next
            else:
                val = v1
                l1 = l1.next

            current = ListNode(val, None)

            if result == None:
                result = current
                previous = result
            else:
                previous.next = current
                previous = current

        return result
