orders = int(input())
count = 0

for i in range(orders) :
    vps = input()
    for j in range(len(vps)):

        if vps[j] == '(':
            count +=1
        elif vps[j] == ')':
            count -= 1

    if count == 0 :
        print("YES")
    else :
        print("NO")
        
    count = 0

