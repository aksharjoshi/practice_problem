# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import sys

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head_l1 = l1
        head_l2 = l2
        new_list = ListNode()
        head_new_list = new_list
        while head_l1 or head_l2:
            data_l1 = head_l1.val if hasattr(head_l1, 'next') else sys.maxint
            data_l2 = head_l2.val if hasattr(head_l2, 'next') else sys.maxint

            if data_l1 <= data_l2:
                temp_list = ListNode(data_l1)
                new_list.next = temp_list
                head_l1 = head_l1.next if hasattr(head_l1, 'next') else None
                new_list = new_list.next
            elif data_l2 < data_l1:
                temp_list = ListNode(data_l2)
                new_list.next = temp_list
                head_l2 = head_l2.next if hasattr(head_l2, 'next') else None
                new_list = new_list.next
            
        return head_new_list.next
                
            
            
            
            
            
        