# Definition for singly-linked list.
# class ListNode(object):
# def __init__(self, val=0, next=None):
# self.val = val
# self.next = next
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head, k):
        def reverseLinkedList(head, k):
            prev, curr = None, head
            while k:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
                k -= 1
            return prev
        
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy
        
        while True:
            kth = group_prev
            count = 0
            while count < k and kth:
                kth = kth.next
                count += 1
            if not kth:
                break
            
            group_next = kth.next
            prev, curr = group_next, group_prev.next
            for _ in range(k):
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            tmp = group_prev.next
            group_prev.next = prev
            group_prev = tmp
        
        return dummy.next
