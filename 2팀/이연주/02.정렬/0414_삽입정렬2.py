N, K = tuple(map(int, input().split()))
arrA = list(map(int, input().split()))
sorted_arr = sorted(arrA)
cnt = 0
answer = -1

for i in range(1, N):
    loc = i-1 # 삽입 위치를 찾는 변수
    insert_num = arrA[i] # 삽입할 숫자

    if arrA == sorted_arr:
        break

    while loc >= 0 and arrA[loc] > insert_num: 
        arrA[loc+1] = arrA[loc]
        loc -= 1
        cnt += 1
        if cnt == K :
            answer = 0
            break

    if loc + 1 != i and answer != 0:
        arrA[loc + 1] = insert_num
        cnt += 1

    if cnt == K:
        answer = 0
        break


if answer == 0:
    print(*arrA)
else:
    print(-1)