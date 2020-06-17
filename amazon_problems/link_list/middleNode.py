# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        lenList = self.calcLen(head)
        
        if lenList == 0:
            raise Exception('empty')
        
        if lenList % 2 != 0:
            mid = lenList / 2
        else:
            mid = round((float)(lenList) / 2)
        
        count = 0
        
        while count < mid:
            head = head.next
            count += 1
        
        return head
    
    def calcLen(self, head):
        tempHead = head
        length = 0
        while tempHead:
            length += 1
            tempHead = tempHead.next
        return length
        