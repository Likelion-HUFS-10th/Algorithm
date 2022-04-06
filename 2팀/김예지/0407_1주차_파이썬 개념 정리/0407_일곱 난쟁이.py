h_lst = []

for i in range(9):
    h_lst.append(int(input()))

cnt = sum(h_lst)
a = 0
b = 0

for i in range(8):
    for j in range(i+1, 9):
        if cnt - (h_lst[i] + h_lst[j]) == 100:
            a = h_lst[i]; b = h_lst[j]
            
h_lst.remove(a)
h_lst.remove(b)
for i in range(7):
    print(sorted(h_lst)[i])
