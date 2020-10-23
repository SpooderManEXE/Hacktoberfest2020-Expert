# Node Class
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

# Queue Class
class Queue:

    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.head = None
        self.tail = None

    # Checks if Queue is empty
    def isEmpty(self):
        return self.size == 0

    # Checks if Queue is full
    def isFull(self):
        return self.size == self.capacity

    # Inserts element in the Queue
    def enQueue(self, data):
        if not self.isFull():    
            temp = Node(data)
            if self.isEmpty():
                self.head = temp
                self.tail = temp
            else:
                self.tail.next = temp
                self.tail = temp
            self.size+=1
        else:
            raise NameError("Queue Overflow.")

    # Removes and returns element from the Queue
    def deQueue(self):
        if not self.isEmpty():
            temp = self.head
            if self.size == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
            self.size-=1
            return temp
        else:
            raise NameError("Queue Underflow.")

    # Peeks at the front of the Queue. 
    # Note that this doesn't remove the node. 
    # It only returns the value of the data attribute of
    # Queue's head node.
    def front(self):
        if not self.isEmpty():
            return self.head.data
        else:
            print("Queue is empty.")

    # To print the Queue.
    def print(self):
        if not self.isEmpty():
            represent = "[ "
            temp = self.head
            while temp is not None:
                represent += (str(temp.data) + ", ")
                temp = temp.next
            represent = represent[:len(represent)-2]
            represent += " ]"
            return represent
        else:
            return "Queue is empty."

    # Overriding the __str__() method to represent the Queue
    # without explicitly using the print() method.
    def __str__(self):
        return self.print()


# Usage
q = Queue(5)
q.enQueue(1) # 1
q.enQueue(2) # 1, 2
q.enQueue(3) # 1, 2, 3
q.enQueue(4) # 1, 2, 3, 4
q.enQueue(5) # 1, 2, 3, 4, 5
print(f"Queue state: {q.print()}") # prints "[ 1, 2, 3, 4, 5 ]"
d = q.deQueue() # dequeues and returns the first node
print(f"Dequeued data: {d.data}") # prints "1"
print(f"Queue front: {q.front()}") # prints "2"
q.deQueue() # dequeues and returns the second node
print(f"Queue state: {q}") # Invokes __str__() method and prints "[ 3, 4, 5 ]"
print(f"Queue size: {q.size}") # prints "3"