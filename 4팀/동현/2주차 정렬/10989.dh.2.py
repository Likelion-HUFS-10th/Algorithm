import sys
n = int(input())
array = 10001 * [0]

for i in range(n):
    array[int(sys.stdin.readline())] += 1 # sys.stdin.readline() -> input()의 시간 초과 문제를 해결

for j in range(10001):
    if array[j] != 0:
        for k in range(array[j]):
            print(j)
