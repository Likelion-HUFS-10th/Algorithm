stack = []
err = 0
cnt = 0

while True :
    data = input()
    for i in data :
        if i == "(":
            stack.append(i)
            cnt = 0
        elif i == "[":
            stack.append(i)
            cnt = 1
        elif i == ")" :
            if len(stack) > 0 and cnt == 0:
                stack.pop()
            else :
                err =1
        elif i == "]" :
            if len(stack) > 0 and cnt == 1 :
                stack.pop()
            else :
                err =1
        elif i == ".":
            break

    if len(stack) == 0 and err == 0:
        print("YES")
    else :
        print("NO")
    stack = []
    err = 0

    break

#런타임에러