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
        # 初始化首个节点，p 为 pointer 之意
        head = ListNode(0)
        p = head
        carry = 0
        
        while True:
            
            # 逐个遍历 l1 及 l2 两个链表
            if l1 != None:
                carry += l1.val
                l1 = l1.next
            if l2 != None:
                carry += l2.val
                l2 = l2.next
            
            # 当前的 carry 即为 l1.val, l2.val, carry 三者之和
            p.val = carry % 10
            carry = carry / 10
            
            # 未结束前，都要初始化下一个节点
            if l1 != None or l2 != None or carry != 0:
                p.next = ListNode(0)
                p = p.next
            
            # 否则跳出循环（容易遗漏！）
            else:
                break
            
        return head
                
        