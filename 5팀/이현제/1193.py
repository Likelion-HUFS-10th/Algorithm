def make(q):
    back = q[0]
    q = q[1:n + 1]
    q.append(back)
    return q

def big(a):
    big = 0
    for i in range(len(a)):
        if a[i] >= big:
            big = a[i]
    return big


n, m = tuple(map(int, input().split()))
queue = list(map(int,input().split()))

cnt = 0
while(1):
    list_big = big(queue)
    if queue[0] == list_big:
        queue.pop(0)
        cnt += 1
        print(queue)
    else:
        queue = make(queue)
        cnt += 1
        print(queue)
print(cnt)



