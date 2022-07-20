#함수 선언

def push(num, queue):
    queue.append(num)

def pop(queue):
    if len(queue) == 0 :
        print(-1)
    else :
        print(queue[0])
        queue.remove(queue[0])

def size(queue) :
    print(len(queue))

def empty(queue):
    if len(queue) == 0 :
        print(1)
    else :
        print(0)

def front(queue):
    if len(queue) == 0 :
        print(-1)
    else :
        print(queue[0])

def back(queue):
    if len(queue) == 0 :
        print(-1)
    else :
        print(queue[len(queue)-1])


queue = []
order = ""

orders = int(input())

for i in range(orders):
    order = input()
    if len(order)>5 :
        a,b = order.split()
        push(b,queue)
    elif order == "front":
        front(queue)
    elif order == "back":
        back(queue)
    elif order == "pop":
        pop(queue)
    elif order == "size":
        size(queue)
    elif order == "empty":
        empty(queue)
