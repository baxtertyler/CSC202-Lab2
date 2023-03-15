class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:

    def __init__(self, capacity):
        self.capacity = capacity
        self.top = None
        self.num_items = 0

    def is_empty(self):
        return self.num_items == 0

    def is_full(self):
        return self.num_items == self.capacity

    def push(self, item):
        if self.is_full():
            raise IndexError
        else:
            self.num_items += 1
            n = Node(item)
            n.next = self.top
            self.top = n

    def pop(self):
        if self.is_empty():
            raise IndexError
        else:
            self.num_items -= 1
            self.top = self.top.next

    def peek(self):
        if self.is_empty():
            raise IndexError
        else:
            return self.top.data

    def size(self):
        return self.num_items
