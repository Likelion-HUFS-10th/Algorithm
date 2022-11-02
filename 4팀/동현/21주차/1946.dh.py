"""
서류 or 면접 하나라도 떨어지지 않는다면 선발
선발 가능한 최대 인원수 구하기
"""
import copy
t = int(input())
n = int(input())

score_list = []

for i in range(n):
    score_list.append(list(map(int,input().split())))

result = 0

for i in range(n):
    copy_score = copy.deepcopy(score_list)
    target = copy_score[i][0]
    copy_score.pop(i)
    flag = True
    for j in range(len(copy_score)):
        if target >= copy_score[j][0]:
            pass
        else:
            flag = False
    if flag == True:
        result += 1
    else:
        target = copy_score[i][1]
        flag = True
        for j in range(len(copy_score)):
            if target >= copy_score[j][1]:
                pass
            else:
                flag = False
        if flag == True:
            result += 1
        else:
            pass
        
print(result)




