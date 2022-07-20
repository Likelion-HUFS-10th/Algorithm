#함수 선언

def push(num, stacked):
    stacked.append(num)

def pop(stacked):
    if len(stacked) == 0 :
        print(-1)
    else :
        print(stacked[len(stacked)-1])
        stacked.remove(stacked[len(stacked)-1])


def size(stacked) :
    print(len(stacked))

def empty(stacked):
    if len(stacked) == 0 :
        print(1)
    else :
        print(0)

def top(stacked):
    if len(stacked) == 0 :
        print(-1)
    else :
        print(stacked[len(stacked)-1])


stacked = []
order = ""

orders = int(input())



for i in range(orders):
    order = input()
    if len(order)>5 :
        a,b = order.split()
        push(b,stacked)
    elif order == "top":
        top(stacked)
    elif order == "pop":
        pop(stacked)
    elif order == "size":
        size(stacked)
    elif order == "empty":
        empty(stacked)
