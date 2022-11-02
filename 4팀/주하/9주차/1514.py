# 잃어버린 괄호
letter = input().split('-')
minus_list = []

for i in letter:
    s = 0
    plus = i.split('+')
    for j in plus:
        s += int(j)
    minus_list.append(s)

first = minus_list[0]

for i in range(1, len(minus_list)):
    first = first - minus_list[i]

print(first)
