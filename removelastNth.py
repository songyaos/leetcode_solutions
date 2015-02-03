# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        if head == None:
            return head
        
        cnt = 0;
        plist=[]
        current=head
        while(current!=None):
            cnt = cnt+1
            plist.append(current)
            current = current.next
        
        if cnt ==n:
            return head.next
        if n==1:
            plist[cnt-2].next=None
            return head
            
        
        plist[cnt-n-1].next = plist[cnt-n].next
        return head
        