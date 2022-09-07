# 처음에는 약수를 구해서 어떤 수를 2, 3, 5라는 소수의 제곱으로만 표현하고자 했다
# 하지만 반복문 구현 방법을 찾지 못했다

x = int(input())

d = [0] * 30001

for i in range(2, x+1):
    d[i] = d[i - 1] + 1
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2] + 1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3] + 1)
    if i % 5 == 0:        
        d[i] = min(d[i], d[i//5] + 1)

print(d[x])