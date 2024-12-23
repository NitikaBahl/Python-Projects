class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    dummy_head = ListNode()  
    current = dummy_head
    carry = 0

    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        
        total = val1 + val2 + carry
        carry = total // 10
        current.next = ListNode(total % 10)
        current = current.next
        

        if l1: l1 = l1.next
        if l2: l2 = l2.next

    return dummy_head.next

def createLinkedList(nums):
    dummy = ListNode()
    current = dummy
    for num in nums:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

def printLinkedList(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

if __name__ == "__main__":
    l1 = createLinkedList([2, 4, 3]) 
    l2 = createLinkedList([5, 6, 4])  
    result = addTwoNumbers(l1, l2)    
    printLinkedList(result)