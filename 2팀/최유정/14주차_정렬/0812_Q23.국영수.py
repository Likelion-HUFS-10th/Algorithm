import sys
input = sys.stdin.readline

n = int(input())
score = []
for _ in range(n):
    name, korean, english, math = input().split()
    score.append([name, int(korean), int(english), int(math)])

score.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for student in score:
    print(student[0])