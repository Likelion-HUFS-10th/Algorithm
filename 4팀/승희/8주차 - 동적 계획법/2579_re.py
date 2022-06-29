'''
한번에 두개 혹은 한개
연속된 세개 x
마지막 계단 반드시
'''

n = int(input()) #계단의 개수
stairs = [0]

for _ in range(n):
    stairs.append(int(input()))

if n==1:
    print(stairs[1])
else:
    arr = [0]*(n+1)

    arr[1] = stairs[1]
    arr[2] = stairs[1]+stairs[2]

    for i in range(3,n+1):
        arr[i] = max(arr[i-3]+stairs[i-1]+stairs[i],arr[i-2]+stairs[i])

    # arr[0] = stairs[0]
    # arr[1] = arr[0]+stairs[1]

    # for i in range(2,n):
    #     arr[i] = max(arr[i-1],arr[i-2]+stairs[i])

    print(arr[n])