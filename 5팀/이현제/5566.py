n, m = tuple(map(int, input().split()))
order = [
    int(input())
    for _ in range(n)
]

dice = [ 
    int(input())
    for _ in range(m)
]

pointer = 0
cnt = 0

for i in dice:
    cnt += 1
    pointer += i
    if pointer >= n - 1:
        print(cnt)
        break
    pointer += order[pointer]
    if pointer >= n - 1:
        print(cnt)
        break