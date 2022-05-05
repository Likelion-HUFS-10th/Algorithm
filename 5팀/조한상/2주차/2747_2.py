n = int(input())
fnum_list = [0,1]
for i in range(2, n+1):
    fnum_list.append(fnum_list[-1]+fnum_list[-2])

print(fnum_list[n])