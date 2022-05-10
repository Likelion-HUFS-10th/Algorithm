n = int(input())
orders = [
    tuple(input().split())
    for _ in range(n)
]
arr = []

for i in range(n):
    if len(orders[i])==2:
        order,num = orders[i]
    else:
        order = orders[i][0]

    if order=="push":
        arr.append(int(num))
    elif order=="pop":
        if not arr:print(-1)
        else:
            result_num = arr.pop()
            print(result_num)
    elif order=="size":
        print(len(arr))
    elif order=="empty":
        if arr:print(0)
        else:print(1)
    elif order=="top":
        if arr: print(arr[-1])
        else: print(-1)