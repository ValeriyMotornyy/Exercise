class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class LinkedList:

    def __init__(self):
        self.head = None
        self.curr = None
        self.tail = None

    def __iter__(self):
        return self

    def next(self):
        if self.head and not self.curr:
            self.curr = self.head
            return self.curr
        elif self.curr.next:
            self.curr = self.curr.next
            return self.curr
        else:
            raise StopIteration

    def append(self, data):
        n = Node(data)
        if not self.head:
            self.head = n
            self.tail = n
        else:
            self.tail.next = n
            self.tail = self.tail.next


# Add 5 nodes
linkedList = LinkedList()
for i in range(1, 6):
    linkedList.append(i)

# print out the list
for node in linkedList:
    print node
