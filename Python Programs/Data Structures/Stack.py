# Node Class
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    # Overriding __str__ method to change the way Node class objects are represented in String
    def __str__(self):
        return f"Node with:\n\tData: {self.data}\n\tNext: {self.next}"

# Stack Class
class Stack: 

    def __init__(self, capacity):
        if capacity == 0:
            raise ValueError("Capacity cannot be Zero.")
        else:
            self.capacity = capacity
            self.size = 0
            self.first = None # Stack pointer
    
    # Checks if Stack is Empty
    def isEmpty(self):
        return self.size == 0
    
    # Checks if Stack is Full
    def isFull(self):
        return self.size == self.capacity

    # Inserts element into Stack
    def push(self, data):
        if not self.isFull():
            temp = Node(data)
            temp.next = self.first
            self.first = temp
            self.size+=1
        else:
            raise NameError("Stack Overflow.")

    # Removes and return the Node element pointed by the Stack pointer
    def pop(self):
        if not self.isEmpty():
            temp = self.first
            self.first = self.first.next
            temp.next = None
            self.size-=1
            return temp
        else:
            raise NameError("Stack Underflow.")

    # Returns the data stored in the Node pointed by the stack pointer
    def peek(self):
        if not self.isEmpty():
            return self.first.data
        else:
            return "Stack is Empty"

    # Print function to represent the Stack in String
    def print(self):
        if not self.isEmpty():
            represent = "[ "
            temp = self.first
            while temp is not None:
                represent += (str(temp.data) + ", ")
                temp = temp.next
            represent = represent[:len(represent)-2] + " ]"
            return represent
        else:
            return "Stack is Empty"

    # Overriding __str__ method to return same as print() method
    def __str__(self):
        return self.print()


# Usage
s = Stack(5) # Create a new Stack
s.push(1) # 1
s.push(2) # 2, 1
s.push(3) # 3, 2, 1
s.push(4) # 4, 3, 2, 1
s.push(5) # 5, 4, 3, 2, 1
print(f"Stack state: {s.print()}") # Prints 'Stack state: [ 5, 4, 3, 2, 1 ]'
print(f"Peek: {s.peek()}") # Prints 'Peek: 5'
print(f"Popped: {s.pop()}") # Prints 'Popped: Node with:
                            #                 Data: 5
                            #                 Next: None'
print(f"Stack state: {s}") # Prints 'Stack state: [ 4, 3, 2, 1 ]'
while not s.isEmpty():
    print(f"Popped: {s.pop()}")
    print(f"Stack state: {s}")
