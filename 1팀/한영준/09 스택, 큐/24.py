class MyStack :

    def __init__(self) -> None:
        self.stack = []

    def push(self, a) :
            self.stack.append(a)
            
    def pop(self):
        return self.stack.pop(0)

    def peek(self):
        return self.stack[0]

    def empty(self):
        return len(self.stack) == 0

queue = MyStack()

queue.push(1)
queue.push(2)
print(queue.peek())
print(queue.pop())
print(queue.pop())
print(queue.empty())