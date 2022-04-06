x, y = map(int, input().split())
lst = []
for i in range(y+1) :
    for j in range(i):
        if len(lst) == y:
            break
        lst.append(i)
print(sum(lst[x-1:y]))