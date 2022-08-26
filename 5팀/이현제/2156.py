n = int(input())
wine = [
    int(input())
    for _ in range(n)
]

wine_dp = [0] * n
result = 0

if n == 1:
    result = wine[0]
elif n == 2:
    result = wine[0] + wine[1]
    
for i in range(2, n):
    
