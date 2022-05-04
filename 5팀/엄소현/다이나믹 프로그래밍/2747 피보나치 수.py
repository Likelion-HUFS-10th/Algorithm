import sys
input = sys.stdin.readline

n = int(input())
fib = [0 for _ in range(n+1)]

for i in range(n+1):
    if i == 0 or i == 1:
        fib[i] = i
    else:
        fib[i] = fib[i-1] + fib[i-2]

print(fib[n])
