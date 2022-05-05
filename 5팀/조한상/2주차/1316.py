num = int(input())

for i in range(num):
    word = input()
    for j in range(len(word)-1):
        if word[j] != word[j+1]:
            if word[j] in word[j+1: ]:
                num -= 1
                break
print(num)