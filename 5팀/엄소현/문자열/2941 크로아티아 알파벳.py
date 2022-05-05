import sys
input = sys.stdin.readline

word = input().strip()
cnt = 0   # 문자 개수

for i in range(len(word)):
    if word[i] == '-':
        continue
    elif word[i] == '=':
        if i > 1 and word[i-2:i] == 'dz':
            cnt -= 1
            continue
        continue
    elif word[i] == 'j':
        if i > 0 and word[i-1] == 'l' or word[i-1] == 'n':
            continue
    cnt += 1

print(cnt)
