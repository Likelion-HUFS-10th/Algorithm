# 신입 사원
T = int(input())
for _ in range(T):
    applica = int(input())
    rank_list = [ list(map(int,input().split())) for _ in range(applica) ]
    rank_list.sort()

    result = 1
    now = rank_list[0][1]
    for i in range(1, applica):
        if now > rank_list[i][1]:
            now = rank_list[i][1]
            result += 1

    print(result)



