# Author : Robert Joseph

from queue import PriorityQueue

class min_max_priority:
    
    def __init__(self):
        self.q = PriorityQueue()
        
    def insert(self,priority_1,value):
        self.q.put((priority_1,value))

    def maximum(self):
        element = self.q.get()
        self.q.put(element)
        return element
    
    def extract_max(self):
        return self.q.get()
    
    def increase_key(self,value,value_updated):
        while self.q.qsize():
            element = self.q.get()
            if element[0] == value:
                values = element[1]
                break
        final = (value_updated,values)
        self.q.put(final)
    
    def convert_min(self):
        length = self.q.qsize()
        while length:
            element = self.q.get()
            final = (-element[0],element[1])
            self.q.put(final)
            length -= 1
    
    def size(self):
        return self.q.qsize()
    
    def __repr__(self):
        print(self.q)
    
pq = min_max_priority()
pq.insert(1,3)
pq.insert(4,4)
pq.insert(10,4)
pq.increase_key(1,2)
print(pq.maximum())
pq.insert(100,4)
pq.convert_min()
pq.__repr__()
print(pq.extract_max())
