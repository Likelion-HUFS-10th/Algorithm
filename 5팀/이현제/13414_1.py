from collections import deque, OrderedDict


k, l = tuple(map(int, input().split()))
student = deque()
for _ in range(l):
    a = input()
    student.appendleft(a)

student = list(student)
student = list(dict.fromkeys(student))

for _ in range(k):
    print(student.pop())
    if len(student) == 0:
        quit()