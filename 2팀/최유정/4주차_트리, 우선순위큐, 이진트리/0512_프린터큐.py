import sys
input = sys.stdin.readline

class PriorityQueue:
    def __init__(self):
        self.items =[]

    def isEmpty(self):
        return len(self.items) == 0
    def enqueue(self, item):
        self.items.append(item)
    def size(self): return len(self.items)

    def findMaxIndex(self):
        if self.isEmpty(): return None
        else:
            hightest = 0
            for i in range(1, self.size()):
                if self.items[i][0] > self.items[hightest][0]:
                    hightest = i
            for _ in range(hightest):
                self.items.append(self.items.pop(0))
            return self.items.pop(0)

t = int(input())

for _ in range(t):
    q = PriorityQueue()
    print_num = 1
    n, m = map(int, input().split())
    list_num = list(map(int, input().split()))

    cnt = 0
    for i in list_num:
        q.enqueue([i, cnt])
        cnt += 1

    while not q.isEmpty():
        if q.findMaxIndex()[1] == m:
            print(print_num)
        print_num += 1