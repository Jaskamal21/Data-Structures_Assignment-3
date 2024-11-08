class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class MyList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def remove_last(self):
        if self.head is None:
            print("List is empty. No nodes to remove.")
            return
        if self.head.next is None:
            self.head = None
        else:
            current = self.head
            while current.next.next:
                current = current.next
            current.next = None

    def __str__(self):
        values = []
        current = self.head
        while current:
            values.append(str(current.data))
            current = current.next
        return " -> ".join(values) if values else "Empty List"


my_list = MyList()
my_list.add(5)
my_list.add(7)
my_list.add(10)

my_list.remove_last()

print(my_list)
