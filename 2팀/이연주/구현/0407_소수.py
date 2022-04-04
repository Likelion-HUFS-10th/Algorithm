M = int(input())
N = int(input())

def sosu(k):
    for i in range(2, k):
        if k % i == 0:
            return False
    return True

sum, minimum = 0, 0
if M == 1:
    M += 1

for i in range(M, N+1):
    if sosu(i):
        sum += i
        if minimum == 0:
            minimum = i

if sum != 0:
    print(sum)
    print(minimum)
else:
    print(-1)