"""
규칙을 살펴보면 피보나치 수열과 유사
"""
t = int(input())

for _ in range(t):
    n = int(input())
    d = [0] * 1000
    d[1] = 1
    d[2] = 2
    d[3] = 4
    for i in range(4,n+1):
        d[i] = d[i-3] + d[i-2] + d[i-1]
    print(d[n])