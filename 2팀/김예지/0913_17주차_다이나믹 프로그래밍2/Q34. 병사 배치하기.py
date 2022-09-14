n = int(input())
array = list(map(int, input().split()))
result = []
start = 1

while len(array) > 1:
    judge = [False for _ in range(len(array))]
    judge[0] = True
    cnt = 0

    pointer = array[0]
    for i in range(start, len(array)):
        if pointer > array[i]:
            judge[i] = True
            cnt += 1
            pointer = array[i]

    result.append((len(array), cnt))
    if False in judge:
        start_idx = judge.index(False)
        array = array[start_idx:]
    else:
        break

min = 10001
for r in result:
    if min > r[1]:
        min = r[1]

print(min)

# 틀렸대요..