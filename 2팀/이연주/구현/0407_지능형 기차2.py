info = [tuple(map(int, input().split())) for _ in range(10)]

answer, maximum = 0, 0
for outs, ins in info:
    answer -= outs
    answer += ins
    maximum = max(answer, maximum)
print(maximum)