class DisjointSet:
    def __init__(self):
        self.parent = {}

    def make_set(self, x):
        self.parent[x] = x

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root != y_root:
            self.parent[x_root] = y_root
            
ds = DisjointSet()

ds.make_set(1)
ds.make_set(2)
ds.make_set(3)

print(ds.find(1))  # prints 1
print(ds.find(2))  # prints 2

ds.union(1, 2)
print(ds.find(1))  # prints 2
print(ds.find(2))  # prints 2
