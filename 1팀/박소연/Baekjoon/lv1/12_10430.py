# 입력값 받고 사칙연산

a, b, c = map(int, input().split())

print((a + b) % c)
print(((a % c) + (b % c)) % c)
print((a * b) % c)
print(((a % c) * (b % c)) % c)