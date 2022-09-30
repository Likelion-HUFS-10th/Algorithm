from collections import deque

n = int(input())
results = []
for _ in range(n):
    order = input()
    arr_num = int(input())
    num = input()[1:-1].split(",")
    num = deque(num)
    r = 0
    rst = 0
    for target in order:
        if target == 'R':
            if r == 0:
                r = 1
            else:
                r = 0
        elif target == 'D':
            if arr_num == 0:
                results.append('error')
                rst = 1
                break
            if len(num) == 0:
                results.append('error')
                rst = 1
                break

            if r == 0:
                num.popleft()
            else:
                num.pop()
    if r == 0 and rst != 1:
        results.append(num)
    elif r == 1 and rst != 1:
        num_result = []
        while num:
            num_pop = num.pop()
            num_result.append(num_pop)
        results.append(num_result)

for result in results:
    if result != 'error':
        print('[', end='')
        print(*result, sep=",", end=']\n')
    else:
        print(result)
    

