class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    
    def insert_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node

    
    def insert_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
        new_node.prev = curr

    
    def insert_after(self, prev_node_data, data):
        curr = self.head
        while curr and curr.data != prev_node_data:
            curr = curr.next
        if not curr:
            print("Previous node not found.")
            return
        new_node = Node(data)
        new_node.next = curr.next
        new_node.prev = curr
        if curr.next:
            curr.next.prev = new_node
        curr.next = new_node

    
    def delete(self, key):
        curr = self.head
        while curr and curr.data != key:
            curr = curr.next
        if not curr:
            print("Node not found.")
            return
        if curr.prev:
            curr.prev.next = curr.next
        else:
            self.head = curr.next
        if curr.next:
            curr.next.prev = curr.prev

    
    def traverse_forward(self):
        curr = self.head
        while curr:
            print(curr.data, end=' ')
            curr = curr.next
        print()

    
    def traverse_backward(self):
        curr = self.head
        if not curr:
            return
        while curr.next:
            curr = curr.next
        while curr:
            print(curr.data, end=' ')
            curr = curr.prev
        print()


if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.insert_end(10)
    dll.insert_end(20)
    dll.insert_front(5)
    dll.insert_after(10, 15)

    print("Forward traversal:")
    dll.traverse_forward()

    print("Backward traversal:")
    dll.traverse_backward()

    print("After deleting 10:")
    dll.delete(10)
    dll.traverse_forward()




