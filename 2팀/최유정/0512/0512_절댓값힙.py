import sys
input = sys.stdin.readline

class MinHeap:
    def __init__(self):
        self.heap = []
        self.heap.append(0)

    def size(self): return len(self.heap)-1
    def isEmpty(self): return self.size() == 0
    def Parent(self, i): return self.heap[i//2]
    def Left(self, i): return self.heap[i*2]
    def Right(self, i): return self.heap[i*2 + 1]

    def insert(self, n):
        self.heap.append(n)
        i = self.size()
        while (i != 1 and abs(n) <= abs(self.Parent(i))):
            if abs(n) == abs(self.Parent(i)) and n > self.Parent(i):
                break
            else:
                self.heap[i] = self.Parent(i)
                i = i // 2
        self.heap[i] = n

    def find(self):
        parent = 1
        child = 2
        if not self.isEmpty():
            hroot = self.heap[1]
            last = self.heap[self.size()]
            while (child <= self.size()):
                if child < self.size() and abs(self.Left(parent)) >= abs(self.Right(parent)):
                    if not (abs(self.Left(parent)) == abs(self.Right(parent)) and self.Left(parent) < self.Right(parent)):
                        child += 1
                if abs(last) <= abs(self.heap[child]):
                    if not (abs(last) == abs(self.heap[child]) and last > self.heap[child]):
                        break
                self.heap[parent] = self.heap[child]
                parent = child
                child *= 2
            
            self.heap[parent] = last
            self.heap.pop(-1)
            return hroot

    

heap = MinHeap()
list_num = []
n = int(input())
for _ in range(n):
    num = int(input())
    if not heap.isEmpty() and num == 0:
        list_num.append(heap.find())
        continue
    if heap.isEmpty() and num == 0:
        list_num.append(0)
        continue
    heap.insert(num)

for i in list_num:
    print(i)