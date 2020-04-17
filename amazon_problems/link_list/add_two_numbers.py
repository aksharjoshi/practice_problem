# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        defaultHead = ListNode()
        currentHead = defaultHead

        p = l1
        q = l2
        carry = 0
        finalHead = currentHead

        while p or q:
        	x = p.val if p else 0
        	y = q.val if q else 0

        	carry, finalnum = divmod(x + y + carry, 10)
        	# carry = sum / 10
        	# finalnum = sum % 10

        	currNode = ListNode(finalnum)
        	currentHead.next = currNode
        	currentHead = currentHead.next
        	p = p.next if p else None
        	q = q.next if q else None

        if carry > 0:
            currentHead.next = ListNode(carry)
            currentHead = currentHead.next

        return finalHead.next