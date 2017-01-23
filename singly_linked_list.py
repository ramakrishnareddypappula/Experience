from __future__ import print_function

class Node(object):
   """Create a node."""
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

class SingleLinkedList(object):
    """Initialize the head."""
    def __init__(self, head=None):
        self.head = head

    # append: insert at the end
    def append(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
        temp = self.head
        while temp.next_node is not None:
            temp = temp.next_node
        if self.head is not node:
            temp.next_node = node

    # insert: insert at the begining
    def insert(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
        else:
            node.next_node = self.head
            self.head = node

    # nposition: insert at the nth position
    def nposition(self, value, position):
        temp1 = Node(value)
        if position == 1:
            temp1.next_node = self.head
            self.head = temp1
            return
        temp2 = self.head
        for i in xrange(0, position - 2):
            temp2 = temp2.next_node
        temp1.next_node = temp2.next_node
        temp2.next_node = temp1

    # display the singly linked list            
    def display(self):
        temp = self.head
        print('\n')
        while temp:
            print(str(temp.data)+'->',end="")
            temp = temp.next_node
        print(None)

    # return the size of the list
    def size(self):
        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.next_node
        print(count)

    # Delete the nth position in the list
    def delete(self, position):
        temp = self.head
        if position == 1:
            self.head = temp.next_node
            return
        for i in range(0, position - 2):
            temp = temp.next_node
        temp2 = temp.next_node
        temp.next_node = temp2.next_node

    # Reverse list usign iteration
    def iterative_reverse(self):
        current = self.head
        prev = None
        while current:
            nnext = current.next_node
            current.next_node = prev
            prev = current
            current = nnext
        self.head = prev
        return self.head

    # print using recursion
    @staticmethod
    def print_recursive(head):
        if head is None:
            return
        print(' {} '.format(head.data))
        SingleLinkedList.print_recursive(head.next_node)

    # print reverse using recursion
    @staticmethod
    def print_reverse_recursion(head):
        if head is None:
            return
        SingleLinkedList.print_reverse_recursion(head.next_node)
        print(' {} '.format(head.data)) 

s = SingleLinkedList()
s.append(10)
s.append(20)
s.append(30)
s.insert(50)
s.insert(60)
s.insert(90)
s.display()
s.size()
s.insert(40)
s.display()
s.size()
s.nposition(2, 1)
s.nposition(3, 2)
s.nposition(4, 1)
s.nposition(5, 2)
s.nposition(10, 3)
s.nposition(12, 5)
s.display()
s.delete(2)
s.display()
s.delete(1)
s.display()
s.iterative_reverse()
s.display()
s.print_recursive(s.head)
s.print_reverse_recursion(s.head)
