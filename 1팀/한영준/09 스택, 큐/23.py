#deque 사용

# import collections

# class MyStack :

#     def __init__(self) -> None:
#         self.q = collections.deque()

#     def push(self, a) :
#         self.q.append(a)
#         for i in range(len(self.q)-1):
#             self.q.append(self.q.popleft())

#     def pop(self):
#         return self.q.popleft()

#     def top(self):
#         return self.q[0]

#     def empty(self):
#         return len(self.q) == 0


class MyStack :
    #리스트 사용

    def __init__(self) -> None:
        self.q = []

    def push(self, a) :
        self.q.append(a)
        
    def pop(self):
        return self.q.pop()

    def top(self):
        return self.q[len(self.q)-1]

    def empty(self):
        return len(self.q) == 0

stack = MyStack()

stack.push(1)
stack.push(2)
print(stack.top())
print(stack.pop())
stack.empty()
