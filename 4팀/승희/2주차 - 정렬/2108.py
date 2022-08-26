import sys

input = sys.stdin.readline

n = int(input()) # 숫자의 개수
arr = [
    int(input())
    for _ in range(n)
]

arr.sort()

avg = sum(arr)/n
avg = round(avg, 0)
print(int(avg))

mid = arr[n//2]
print(mid)

num_arr = []

bef = arr[0]
cnt = 1

for i in range(1,len(arr)):
    if bef == arr[i]:
        cnt +=1
    else:
        num_arr.append((arr[i-1],cnt))
        cnt = 1
        bef = arr[i]
num_arr.append((arr[-1],cnt))

num_arr.sort(key=lambda x: x[1], reverse=True)

if len(num_arr)==1 or num_arr[0][1] != num_arr[1][1]:
    print(num_arr[0][0])
else:
    print(num_arr[1][0])

range = arr[-1] - arr[0]
print(range)

