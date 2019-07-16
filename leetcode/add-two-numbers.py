import typing

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        current1 = l1
        current2 = l2
        
        resultPointer = ListNode(0)
        sumNode = resultPointer
        carryOver = 0

        while current1 != None or current2 != None:
            twoDigitsSum = carryOver

            if current1 != None:
                twoDigitsSum += current1.val
                current1 = current1.next

            if current2 != None:
                twoDigitsSum += current2.val
                current2 = current2.next

            carryOver = int(twoDigitsSum / 10)
            twoDigitsSum = twoDigitsSum % 10

            sumNode.next = ListNode(twoDigitsSum)
            sumNode = sumNode.next

        if carryOver > 0:
            sumNode.next = ListNode(carryOver)

        return resultPointer.next
