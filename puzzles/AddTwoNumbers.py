# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self,lst):
        curr = lst
        next1 = curr.next
        while next1 != None:
            next2 = next1.next ;#save next1 
            next1.next = curr  ;#flip diretion
            curr = next1       ;#curr is next
            next1 = next2      ;#move next1 to next2
        lst.next = None
        return curr
    
    def printList(self, lst):
        l = []
        while lst != None:
            l.append(lst.val)
            lst = lst.next
        print(l)
        
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1p = l1;
        l2p = l2;
        
        c = 0;
        head = None
        curr = head; 
        while l1p != None or l2p != None or c > 0:
            v1 = l1p.val if l1p else 0;
            v2 = l2p.val if l2p else 0;
            d = c + v1 + v2;
            c = d//10;
            d = d % 10;
            node = ListNode(d);
            if head == None:
                head = curr = node
            else:
                curr.next = node
                curr = node
                
            if l1p:
                l1p = l1p.next
            if l2p:
                l2p = l2p.next
        
        return head;
        
            
            
        
        
        
        
        
        
        
        
        