# (3) = a * b[2] 
# (4) = a * b[1] 
# (5) = a * b[0]
# (6) = (3) * 1 + (4) * 10 + (5) * 100

a = int(input())
b = list(input())

num3 = a * int(b[2])
num4 = a * int(b[1])
num5 = a * int(b[0])
num6 = num3 * 1 + num4 * 10 + num5 * 100

print(num3)
print(num4)
print(num5)
print(num6)