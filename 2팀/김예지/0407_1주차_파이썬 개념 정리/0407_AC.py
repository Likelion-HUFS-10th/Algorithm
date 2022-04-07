T = int(input())
for i in range(T):

    func = input()
    cnt = int(input())
    arr = input().replace("[", "").replace("]", "")
    list = arr
    lst = [w.strip() for w in arr.split(",")]

    for i in range(len(func)):
        if func[i] == "R":
            lst = lst[::-1]
        else:
            if (bool(lst) == False) or cnt == 0:
                print("error")
            else:
                lst = lst[1::]

    if bool(lst) != False and cnt !=0 :
        print("[", end="")
        for i in range(len(lst)-1):
            print(lst[i], end=",")
        print(lst[-1]+"]")

# 답은 나오지만 시간초과 에러 뜸.