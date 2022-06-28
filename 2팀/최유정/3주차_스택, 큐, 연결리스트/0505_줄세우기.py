import sys
input = sys.stdin.readline

student_num = int(input())
num_ticket = list(map(int, input().split()))
new_line = []

for i in range(student_num):
    if num_ticket[i] > 0:
        new_line.insert(i - num_ticket[i], i+1)
        continue
    new_line.append(i+1)
for i in range(student_num):
    print(new_line[i], end=' ')