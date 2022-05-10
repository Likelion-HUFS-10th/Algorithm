n = input()

leng = len(n)
leng_minus = leng - 1
output = 0

for i in range(leng - 1):
    output += 9 * (10 ** i) * (i + 1)

output += (int(n) - (10 ** leng_minus) + 1) * leng

print(output)