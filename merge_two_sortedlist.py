# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        result = ListNode(0)
        head = result
        while(l1!=None and l2!=None):
                if l1.val<l2.val:
                    result.next= l1
                    l1 = l1.next
                else :
                    result.next = l2
                    l2 = l2.next
                result =result.next
        if l1==None:
            result.next = l2
        else:
            result.next =l1
        return head.next
        