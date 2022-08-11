n, k = map(int, input().split())
flist = list(map(int, input().split()))
slist = list(map(int, input().split()))

flist.sort()
slist.sort(reverse=True)
for i in range(k):
    if flist[i] < slist[i]:
        flist[i], slist[i] = slist[i], flist[i]
    else:
        break
print(sum(flist))