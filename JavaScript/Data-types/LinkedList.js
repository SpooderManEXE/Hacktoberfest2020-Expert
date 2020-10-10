/**
 * Linked lists are created on non-continuous memory locations
 * 
 * See below their structure:
 * [value, next] -> [value, next] -> [value, next]
 * 
 * Where the first [value, next] pair is called a head. 
 */
class LinkedList {
    
    constructor(data, next = null) {
        this.data = data;
        this.next = next;
    }

    /**
     * Set the next linkedList item
     * 
     * @param {LinkedList} next 
     */
    setNext(next) {
        this.next = next;
    }

    /**
     * Get the next value
     */
    getNext() {
        return this.next;
    }
}

/**
 * Example of linked list:
 * 
 * let linkedList = new LinkedList(1);
 * linkedList.setNext(new LinkedList(2));
 * linkedList.getNext().setNext(new LinkedList(5));
 * console.log(linkedList);
 */