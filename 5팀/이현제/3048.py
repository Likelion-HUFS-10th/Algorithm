n, m = tuple(map(int, input().split()))
input_a = list(input())
a = []
for _ in range(n):
    a.append(input_a.pop())
b = list(input())
t = int(input())
arr = a + b
check = n * '0' + m * '1' + '9'
check_arr = []
target = []

for i in check:
    check_arr.append(i)

for _ in range(t):
    for i in range(n + m):
        if check_arr[i] == '0' and check_arr[i + 1] == '1':
            target.append(i)
    for j in target:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]
        check_arr[j], check_arr[j + 1] = check_arr[j + 1], check_arr[j]
    if not target:
        break
    target = []
    
for i in arr:
    print(i, end='')
