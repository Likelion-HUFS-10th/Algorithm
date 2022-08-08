t = int(input())
arr = [] 
r = 0

for i in range(t):  
    p = list(input())
    n = int(input())
    list = input()

    for k in list[1:-1].split(","): #양쪽 끝의 괄호 제거하고 콤마 단위로 나눔
        arr.append(k)
    
    for j in p:
        if j == "R":
            r += 1
        elif j == "D" and len(arr) == 0:
            print("error")
            break 
        else: #j가 D이면서 빈 배열이 아닌 경우
            if r % 2 == 0:
                arr.pop(0)
            else:
                arr.pop()

    if r % 2 == 1:
        arr.reverse() 
          
    print("[" + ",".join(list(arr)) + "]")