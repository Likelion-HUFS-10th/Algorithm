t = int(input())
tcs = []
for _ in range(t):
    x = int(input())
    tcs.append(x)

# (fb(1) 호출 횟수, fb(0) 호출 횟수)
fb = [(1, 0)] * 41
fb[0] = (0, 1)
fb[1] = (1, 0)

for i in range(2, 41):
    fb[i] = (fb[i-1][0] + fb[i-2][0], fb[i-1][1] + fb[i-2][1])

for tc in tcs:
    print(fb[tc][1], fb[tc][0])