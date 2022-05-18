import sys
input=sys.stdin.readline


def func1(start):
    new_sen = [start+1]
    n_sen = sen[start]
    while True:
        if n_sen not in new_sen:
            new_sen.append(n_sen)
            n_sen = sen[n_sen - 1]
        else:
            return new_sen



n = int(input())
sen = []
max = 0

for i in range(n):
    sen.append(int(input()))

for j in range(n):
    len_sen = len(func1(j))
    if max < len_sen:
        max = len_sen
        sen_num = j + 1

print(sen_num)