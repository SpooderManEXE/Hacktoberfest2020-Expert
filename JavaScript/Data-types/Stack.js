// Node class
class Node {
    constructor(data) {
        this.data = data;
        this.next = null;
    }
}

// Stack class
class Stack {
    constructor(size) {
        if (size === 0) {
            throw Error("Size cannot be Zero.");
        } else {
            this.size = size;
            this.length = 0;
            this.first = null; // this.first is the Stack pointer
        }
    }

    // Checks if Stack is empty
    isEmpty() {
        return this.length === 0;
    }

    // Checks if stack is full
    isFull() {
        return this.length === this.size;
    }

    // Inserts data into Stack
    push(data) {
        if (!this.isFull()) {
            let tempNode = new Node(data);
            tempNode.next = this.first;
            this.first = tempNode;
            this.length += 1;
        } else {
            throw Error("Stack Overflow.");
        }
    }

    // Removes and returns the Node pointed by this.first from the Stack.
    pop() {
        if (!this.isEmpty()) {
            let tempNode = this.first;
            this.first = this.first.next;
            tempNode.next = null;
            this.length -= 1;
            return tempNode;
        } else {
            throw Error("Stack Underflow.");
        }
    }

    // Returns the data stored in the first node of the Stack.
    // Please note: this function doesn't removes the node from the stack.
    peek() {
        if (!this.isEmpty()) {
            return this.first.data;
        } else {
            return "Stack is empty.";
        }
    }

    // Traverses and prints the Stack.
    print() {
        if (!this.isEmpty()) {
            let tempNode = this.first;
            let str = "[ ";
            while (tempNode !== null) {
                str += (tempNode.data + ", ");
                tempNode = tempNode.next;
            }
            str = str.slice(0, str.length - 2) + " ]";
            return str;
        } else {
            return "Stack is empty";
        }
    }
}

// Usage
const s = new Stack(5); // Stack { size: 5, length: 0, first: null }
s.push(1); // 1
s.push(2); // 2, 1
s.push(3); // 3, 2, 1
s.push(4); // 4, 3, 2, 1
s.push(5); // 5, 4, 3, 2, 1
s.push(6); // Error: Stack Overflow.
s.print(); // Prints '[ 5, 4, 3, 2, 1 ]'
s.pop(); // Node { data: 5, next: null }
s.peek(); // 4