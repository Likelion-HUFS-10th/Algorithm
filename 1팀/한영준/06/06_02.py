import sys
n= int(sys.stdin.readline())
num = sys.stdin.readline()
hap = 0

for i in range(n):
    hap = hap+int(num[i])

print(hap)