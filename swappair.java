/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode swapPairs(ListNode head) {
        if (head ==null || head.next ==null) 
            {return head;}
   
        ListNode first = head;
        ListNode second = head.next;
        ListNode newhead = head.next;
        ListNode temp=null;
        while(true){
            //reverse current pair
            first.next = first.next.next;
            second.next = first;
            //for next pair
            //check null condition first
            if (first.next ==null || first.next.next ==null){return newhead;}
            //if we have next pair
            temp = first;//keep the current first pointer
			//move the pointers to the next pair.
            first = first.next;
            second = first.next;
            temp.next = second;//make sure we point from the current pair to the next pair.
            
        }
    
        
    }
}