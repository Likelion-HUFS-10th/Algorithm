a = int(input())
b = int(input())
c = a * (b%10)
d = int(a * (b%100 - b%10) / 10)
e = a * (b//100)
print(c)
print(d)
print(e)
print(a*b)