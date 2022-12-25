
# Priority queue implementation
# Priority queue is built on heapq module which is basically binary heap.
from Queue import PriorityQueue # 2.7 python version.

q = PriorityQueue()

q.put(10)
q.put(5)
q.put(20)


while not q.empty():
    print(q.get()) # 5, 10, 20 # by default in sorted order is returned.


q = PriorityQueue()

q.put((4, 'Read'))
q.put((2, 'Play'))
q.put((5, 'Write'))
q.put((1, 'Code'))
q.put((3, 'Study'))

while not q.empty():
    next_item = q.get() # based on priority like Code, Play, Study, Read and Write are returned.
    print(next_item)