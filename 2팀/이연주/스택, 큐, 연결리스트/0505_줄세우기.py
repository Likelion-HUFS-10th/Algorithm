n = int(input())
students = list(map(int, input().split()))
answer = []

for i in range(n):
    go = students[i]
    answer = answer[:i-go] + [i+1] + answer[i-go:]

print(*answer)