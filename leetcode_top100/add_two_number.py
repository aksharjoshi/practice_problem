# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    def addTwoNumbers(self, l1, l2):
        dummyHead = ListNode()
        currHead = dummyHead
        p = l1
        q = l2

        carry = 0

        while not p.next or not q.next:
            x = p.val if p else 0
            y = q.val if q else 0
            sum = x + y + carry
            carry = sum / 10
            final_sum = sum % 10
            currHead.next = ListNode(final_sum)
            currHead = currHead.next
            p = p.next
            q = q.next

        if carry > 0:
            currHead.next = ListNode(carry)
            currHead = currHead.next

        return currHead


    def addTwoNumbersBrute(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = self.traverse(l1)
        num2 = self.traverse(l2)
        target = num1 + num2
        tar_str = str(target)
        tar_str = tar_str[::-1]
        headNode = ListNode(tar_str[0])
        
        nextNode = headNode
        for val in tar_str[1:]:
            final_li = ListNode(val)
            if nextNode.next:
                while nextNode.next:
                    nextNode = nextNode.next
            nextNode.next = final_li
            nextNode = nextNode.next
            
        return headNode

    def traverse(self, li):
        a = ''
        #iter_node = li.next
        while li:
            a = a + str(li.val)
            li = li.next
        rev_num = a[::-1]
        return int(rev_num)