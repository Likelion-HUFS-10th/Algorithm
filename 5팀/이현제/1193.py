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

a = int(input())
answer = []
for _ in range(a):
    n, m = tuple(map(int, input().split()))
    queue = list(map(int,input().split()))
    outqueue = queue[:]
    outqueue[m] = 'target'
    cnt = 0
    while(1):
        list_big = big(queue)
        if queue[0] == list_big:
            queue.pop(0)
            if outqueue.pop(0) == 'target':
                cnt += 1
                break
            cnt += 1
        else:
            queue = make(queue)
            outqueue = make(outqueue)
    answer.append(cnt)
for i in answer:
    print(i)



