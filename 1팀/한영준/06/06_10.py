import sys
n = int(sys.stdin.readline())
dif1 = 0
dif2 = 0
group = 0

for i in range(n):
    word1 = sys.stdin.readline()
    word2 = sorted(word1)

    for k in range(len(word1)-1):
        if word1[k] != word1[k+1]:
            dif1 = dif1+1
    for k in range(len(word2)-1):
        if word2[k] != word2[k+1]:
            dif2 = dif2+1

    if dif1 == dif2:
        group = group+1
        print (group)


print (group)

#그룹단어가 아닐 시에 이후 회차부터 더이상 카운트가 안되는 오류 발생