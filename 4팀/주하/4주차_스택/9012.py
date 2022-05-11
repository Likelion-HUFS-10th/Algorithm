'''
왼쪽 오른쪽 괄호 따로 확인해서
괄호 수가 같으면 yes 아니면 no

왼쪽, 오른쪽 괄호 수 -> 따로 확인
'''
n = int(input())

for i in range(n):
    word = input()
    left=0
    right=0
    for i in range(len(word)):
        if word[i]=='(':
            left +=1
        else:
            right +=1

        if left < right:       # 오른쪽 괄호 수가 더 많은 경우 for문 빠져나오기
            break

    if left==right:            # 왼쪽 오른쪽 괄호 수가 같은 경우 성립
        print("YES")
    else:
        print("NO")            # 한쪽이라도 더 많으면 NO
