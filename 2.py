# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head=ListNode(0)
        tmp=head
        sum=0
        while True:
            if l1!= None:
                sum+=l1.val
                l1=l1.next
            if l2!= None:
                sum+=l2.val
                l2=l2.next
            tmp.val=sum %10
            sum//=10
            if l1==None and l2==None and sum==0:
                break
            tmp.next=ListNode(0)
            tmp=tmp.next
        return head