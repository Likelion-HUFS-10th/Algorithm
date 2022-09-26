g = int(input())
p = int(input())
dock = [0] * (g+1)
yet = []

def find(dock, x):
    if dock[x] != 0: x = find(dock, x-1)
    return x-1

def setting(x, y):
    x = find(dock, x)
    y = find(dock, y)

for i in range(p):
    gn = int(input())
    l = find(dock, gn)
    if l < 0: continue
    dock[l] = i+1

cnt = 0
for d in dock:
    if d != 0: cnt += 1

print(cnt)