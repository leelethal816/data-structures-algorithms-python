from collections import deque

class Queue:
    
    def __init__(self):
        self.buffer = deque()
    
    def enqueue(self, val):
        self.buffer.appendleft(val)
        
    def dequeue(self):
        return self.buffer.pop()
    
    def is_empty(self):
        return len(self.buffer)==0
    
    def size(self):
        return len(self.buffer)
    
    def front(self):
        return self.buffer[-1]

def binary_nums(end_num):
    nums_queue = Queue()
    nums_queue.enqueue("1")
    for i in range(end_num):
        front = nums_queue.front()
        print(front)
        nums_queue.enqueue(front + "0")
        nums_queue.enqueue(front + "1")
        nums_queue.dequeue()

print(binary_nums(10))