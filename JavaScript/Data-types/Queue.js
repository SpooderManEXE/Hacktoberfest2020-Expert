// Node class
class Node {
    constructor(data) {
      this.data = data;
      this.next = null;
    }
  }
  
  // Queue class
  class Queue {
    constructor(size) {
      this.size = size;
      this.length = 0;
      this.first = null;
      this.last = null;
    }
  
    // checks if Queue is empty
    isEmpty() {
      return this.length === 0;
    }
  
    // checks if Queue is full
    isFull() {
      return this.length === this.size;
    }
  
    // To print the Queue data.
    printQueue() {
      if (!this.isEmpty()) {
        let temp = this.first;
        let str = "[ ";
        while (temp !== null) {
          str += temp.data + ", ";
          temp = temp.next;
        }
        str = str.slice(0, str.length - 2) + " ]";
        return str;
      } else {
        console.log("Queue is empty.");
      }
    }
  
    // Inserts element at the last of the Queue
    enQueue(element) {
      if (!this.isFull()) {
        let newNode = new Node(element);
        if (this.last === null) {
          this.last = newNode;
          this.first = newNode;
        } else {
          this.last.next = newNode;
          this.last = newNode;
        }
        this.length += 1;
      } else {
        throw Error("Queue overflow.");
      }
    }
  
    // Removes and returns first element from the Queue. 
    deQueue() {
      if (!this.isEmpty()) {
        let tempData = this.first.data;
        if (this.length === 1) {
          this.first = null;
          this.last = null;
        } else {
          this.first = this.first.next;
        }
        this.length -= 1;
        return tempData;
      } else {
        throw Error("Queue underflow.");
      }
    }
  
    // Peek at the front of the Queue. This doesn't remove element from the Queue
    front() {
      if (!this.isEmpty()) {
        return this.first.data;
      } else {
        console.log("Queue is empty.");
      }
    }
  }
  
  // Usage
  const q = new Queue(3);
  q.enQueue(1); // [ 1 ]
  q.enQueue(2); // [ 1, 2 ]
  q.enQueue(3); // [ 1, 2, 3 ]
  q.printQueue(); // prints '[ 1, 2, 3 ]'
  q.deQueue(); // return and remove first element. Here, 1. After operation: [ 2, 3 ]
  q.front(); // return 1st element without removing. Here: 2
  q.deQueue(); // return and remove first element. Here, 2. After operation: [ 3 ]
  q.deQueue(); // return and remove first element. Here, 3.
  q.deQueue(); // Error: Queue underflow.
  