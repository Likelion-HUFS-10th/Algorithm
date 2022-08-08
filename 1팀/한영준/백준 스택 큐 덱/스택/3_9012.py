# orders = int(input())
# count = 0

# for i in range(orders) :
#     vps = input()
#     for j in range(len(vps)):

#         if vps[j] == '(':
#             count +=1
#         elif vps[j] == ')':
#             count -= 1

#     if count == 0 :
#         print("YES")
#     else :
#         print("NO")
        
#     count = 0

T = int(input())
stack = []
err = 0

for _ in range(T):
    data = input()
    for i in data :
        if i == "(":
            stack.append(i)
        elif i == ")" :
            if len(stack) > 0:
                stack.pop()
            else :
                err +=1
                

    if len(stack) == 0 and err == 0:
        print("YES")
    else :
        print("NO")
    stack = []
    err = 0