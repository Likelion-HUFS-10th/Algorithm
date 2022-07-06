list = [1,2,3,4]
real_list = list
gop = 1
gop_list = []

for i in range(len(list)):
    del list[i]
    for k in range(len(list)):
        gop = gop * list[k]
    gop_list.append(gop)
    gop = 1
    list = real_list

#중첩 반복문 -> O(n^2) ㅠㅠ
    
       
print(gop_list)