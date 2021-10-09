#new line
# Adding new abcd
class queue(object):

    def __init__(self):
        self.list = []

    def push(self, element):
        self.list.insert(0, element)

    def pop(self):
        self.list.pop()

    def display(self):
        return self.list

    def size(self):
        return len(self.list)

s = queue()
s.push(3)
s.push(5)
s.push(6)
s.push(12)
s.push(34)
s.push(64)
print(s.display())
print(s.size())
s.pop()
print(s.display())
s.push(13)
print(s.display())
s.pop()
print(s.display())
s.pop()
print(s.display())
s.pop()
print(s.display())
s.pop()
print(s.display())
