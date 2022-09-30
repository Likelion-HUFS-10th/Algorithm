chess = [[0] * 6 for _ in range(6)]
order = []
cnt = 0
for _ in range(36):
    target = input()
    target = list(target)
    if target[0] == "A":
        target[0] = 1
        target[1] = int(target[1])
        order.append(target)
    elif target[0] == "B":
        target[0] = 2
        target[1] = int(target[1])
        order.append(target)
    elif target[0] == "C":
        target[0] = 3
        target[1] = int(target[1])
        order.append(target)
    elif target[0] == "D":
        target[0] = 4
        target[1] = int(target[1])
        order.append(target)
    elif target[0] == "E":
        target[0] = 5
        target[1] = int(target[1])
        order.append(target)
    elif target[0] == "F":
        target[0] = 6
        target[1] = int(target[1])
        order.append(target)

for x, y in order:
    if cnt != 0:
        if (abs(order[cnt][0] - order[cnt-1][0]) == 1 and abs(order[cnt][1] - order[cnt-1][1]) == 2) or (abs(order[cnt][0] - order[cnt-1][0]) == 2 and abs(order[cnt][1] - order[cnt-1][1]) == 1):
            pass
        else:
            print("Invalid")
            quit()     
    if chess[x-1][y-1] == 1:
        print("Invalid")
        quit()
    elif chess[x-1][y-1] == 0:
        chess[x-1][y-1] = 1
    cnt += 1

if (abs(order[0][0] - order[35][0]) == 1 and abs(order[0][1] - order[35][1]) == 2) or (abs(order[0][0] - order[35][0]) == 2 and abs(order[0][1] - order[35][1]) == 1):
    print("Valid")
else:
    print("Invalid")