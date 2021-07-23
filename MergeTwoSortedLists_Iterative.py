class Solution(object):
    def mergeTwoLists(self, l1, l2):  
        
        dummy = ListNode("Start_Node")
        head=dummy
     
        while l1 != None and l2 != None:
            if l1.val < l2.val:
                dummy.next=l1
                l1=l1.next
            else:
                dummy.next=l2
                l2=l2.next
            dummy=dummy.next
        if l1 == None:
            dummy.next = l2
        else:
            dummy.next = l1
        return head.next
