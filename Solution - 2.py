class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def DLL_len(self):
        length = 0
        current = self.head
        while current:
            length += 1
            current = current.next
        return length


dll = DoublyLinkedList()

dll.add(5)
dll.add(7)
dll.add(13)
dll.add(15)
dll.add(10)

print(dll.DLL_len())
