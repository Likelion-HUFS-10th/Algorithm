n = int(input()) #학생의 수
arr = []

for _ in range(n):
    a, b = input().split()
    b = int(b)
    arr.append((a,b))

arr.sort(key=lambda arr:arr[1])
for i in range(n):
    print(arr[i][0])