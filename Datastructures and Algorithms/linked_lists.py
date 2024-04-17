class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def __contains__(self, data):
        last_node = self.head
        while last_node:
            if data == last_node.data:
                return True
            last_node = last_node.next
        return False

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            last_node.next = Node(data)

    def __getitem__(self, index):
        if index < 0:
            raise IndexError
        last_node = self.head
        i = 0
        while last_node:
            if i == index:
                return last_node.data
            last_node = last_node.next
            i += 1
        raise IndexError

    def remove(self, data):
        last_node = self.head
        if data == last_node.data:
            self.head = self.head.next
            last_node = None
            return
        while last_node.next:
            if data == last_node.next.data:
                temp_node = last_node.next
                if last_node.next.next:
                    last_node.next = last_node.next.next
                else:
                    last_node.next = None
                del temp_node
                return
            last_node = last_node.next
        else:
            raise ValueError

    def print_data(self):
        node = self.head
        while node:
            print(node.data, end=' ')
            node = node.next
        print()
