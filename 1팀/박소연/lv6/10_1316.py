# cnt = num
# 이중 for문 -> 이미 나온 알파벳이 다음 인덱스 이후에 또 나오면 cnt -= 1

num = int(input())
cnt = num

for i in range(num):
  word = input()
  for j in range(len(word)-1):
    if word[j] == word[j+1]:
      pass
    elif word[j] in word[j+1:]:
      cnt -= 1
      break
print(cnt)