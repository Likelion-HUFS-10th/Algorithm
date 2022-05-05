# 크로아티아 알파벳 개수 출력
# 알파벳 리스트 for문 돌려서 elem 마주치면 *로 replace
# len(word) 출력

cro = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
word = input()

for elem in cro :
    word = word.replace(elem, '*')
print(len(word))