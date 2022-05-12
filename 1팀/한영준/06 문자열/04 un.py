import string

paragraph= input()
banned= input()
paragraph = list(paragraph.strip(string.punctuation).lower().split())
#string.punctuation -> '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

if banned in paragraph:
    paragraph = paragraph.remove(banned) #banned 단어 제거

words = list(set(paragraph)) #중복 단어 제거

num1, num2 = 0,0 #등장 횟수 비교를 위한 변수
most = '' #가장 많이 등장한 단어 담아줄 변수

for i in range(len(words)):
    num2 = paragraph.count(paragraph[i])

    if num1<num2:
        num1 = num2
        most = paragraph[i]
    

print(most)