# Node Class
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List class
class LinkedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def getLength(self):
        tempNode = self.head
        length = 0
        while tempNode != None:
            tempNode = tempNode.next
            length += 1
        return length

    def print(self):
        if self.isEmpty():
            return "Linked List is Empty."
        tempNode = self.head
        represent, seperator = "", " -> "
        while tempNode != None:
            represent += f"{tempNode.data}{seperator}"
            tempNode = tempNode.next
        represent += "null"
        return represent

    def insertAtPosition(self, data, position):
        if position < 0:
            raise ValueError("Invalid Position.")
        tempNode = self.head
        previousNode = None
        while position != 0 and tempNode != None:
            position -= 1
            previousNode = tempNode
            tempNode = tempNode.next
        if position != 0:
            #   if the position is not zero, after the loop ends,
            #   it means that the tempNode is None.
            #   So the given position is more than the length of the linked list.
            #   So it is an Invalid position.
            raise ValueError("Invalid Position.")
        newNode = Node(data)
        newNode.next = tempNode
        if previousNode != None:
            previousNode.next = newNode
        else:
            #    if previousNode is None, then the code in loop didn't run
            #    which means the position is 0 or the head is None. So we update the head.
            self.head = newNode

    def insertAtBegining(self, data):
        tempNode = Node(data)
        tempNode.next = self.head
        self.head = tempNode

    def insertAtLast(self, data):
        if self.isEmpty():
            self.insertAtBegining(data)
        else:
            tempNode = Node(data)
            traverseNode = self.head
            while traverseNode.next != None:
                traverseNode = traverseNode.next
            traverseNode.next = tempNode
    
    def deleteAtPosition(self, position):
        if self.isEmpty():
            raise NameError("Empty Linked List.")
        if position < 0:
            raise ValueError("Invalid Position.")
        traverseNode = self.head
        previousNode = None
        while position != 0 and traverseNode.next != None:
            position -= 1
            previousNode = traverseNode
            traverseNode = traverseNode.next
        if position != 0:
            raise ValueError("Invalid Position.")
        if previousNode == None:
            # if previousNode is None, then the code in loop didn't run
            # which means the position is 0. So we update the head.
            self.head = self.head.next
        else:
            previousNode.next = traverseNode.next
        traverseNode.next = None
        return traverseNode

    def deleteAtBegining(self):
        if self.isEmpty():
            raise NameError("Empty Linked List.")
        tempNode = self.head
        self.head = self.head.next
        tempNode.next = None
        return tempNode

    def deleteAtEnd(self):
        if self.isEmpty():
            raise NameError("Empty Linked List.")
        traverseNode = self.head
        previousNode = None
        while traverseNode.next != None:
            previousNode = traverseNode
            traverseNode = traverseNode.next
        if previousNode != None:
            previousNode.next = None
        if self.head == traverseNode:
            self.head = None
        traverseNode.next = None
        return traverseNode

# Usage
ll = LinkedList()
ll.insertAtPosition(1, 0) # 1 -> null
ll.insertAtLast(2) # 1 -> 2 -> -> null
ll.insertAtBegining(0) # 0 -> 1 -> 2 -> null
print(f"{ll.print()}") # prints "0 -> 1 -> 2 -> null"
ll.deleteAtPosition(0);
print(f"{ll.print()}") # 1 -> 2 -> null

ll.insertAtLast(3) # 1 -> 2 -> 3-> null
ll.insertAtPosition(4, ll.getLength()) # 1 -> 2 -> 3 -> 4 -> null

print(f"{ll.print()}") # prints "1 -> 2 -> 3 -> 4 -> null"
print(f"Length = {ll.getLength()}") # prints "Length = 4"

ll.deleteAtPosition(ll.getLength()-1) # 1 -> 2 -> 3 -> null
print(f"{ll.print()}") # prints "1 -> 2 -> 3 -> null"

ll.deleteAtBegining() # 2 -> 3 -> null
print(f"{ll.print()}") # prints "2 -> 3 -> null"

ll.deleteAtEnd() # 2 -> null
print(f"{ll.print()}") # prints "2 -> null"