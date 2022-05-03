"""
회원들의 나이가 증가하는 순으로
나이가 같으면 먼저 가입한 사람이 앞에 오는 순서로
"""

n = int(input()) #몇명인가요
members = []

for i in range(n):
    age,name = input().split()
    age = int(age)
    members.append((age,name))

members.sort(key = lambda x : x[0])

for i in members:
    print(i[0], i[1])