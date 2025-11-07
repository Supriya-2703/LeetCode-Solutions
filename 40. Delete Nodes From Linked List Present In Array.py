class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def modifiedList(self, nums, head):
        """
        Remove all nodes from the linked list whose value is in nums.
        Parameters:
          nums - list[int]
          head - ListNode (head of linked list)
        Returns:
          ListNode - new head after removals
        """
        nums_set = set(nums)          
        dummy = ListNode(0, head)    
        cur = dummy

        while cur.next:
            if cur.next.val in nums_set:
                cur.next = cur.next.next
            else:
                cur = cur.next

        return dummy.next
