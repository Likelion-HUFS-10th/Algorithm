import sys
input = sys.stdin.readline

n = int(input())   # 단어 개수
cnt = 0   # 그룹 단어 개수

for _ in range(n):
    word = input().strip()
    word_zip = set(word[0])   # 단어 첫 번째 문자를 넣은 집합
    cnt += 1
    for i in range(1, len(word)):
        if word[i] not in word_zip:   # 집합에 같은 문자가 없을 경우
            word_zip.add(word[i])
        else:   # 집합에 같은 문자가 있을 경우
            if word[i] == word[i-1]:   # 그 문자가 이전 문자와 같은지 확인
                continue
            else:
                cnt -= 1
                break

print(cnt)
