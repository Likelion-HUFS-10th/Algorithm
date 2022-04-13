N, K = tuple(map(int, input().split()))
arrA = list(map(int, input().split()))
cnt = 0
l = N-1
x, y = 0, 0

while l > 0 :
    last = 0
    for i in range(1, l+1):
        if arrA[i-1] > arrA[i]:
            arrA[i-1], arrA[i] = arrA[i], arrA[i-1]
            last = i
            cnt += 1
            if cnt == K:
                x, y = arrA[i-1], arrA[i]
                break
    l = last
    if cnt == K:
        break

if cnt == K:
    print(x, y)
else:
    print(-1)