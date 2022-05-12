import string

paragraph= input()
banned= input()
paragraph = list(paragraph.strip(string.punctuation).lower().split())

print(paragraph)
if banned in paragraph:
    paragraph = paragraph.remove(banned)

print(paragraph)

words = list(set(paragraph))

num1, num2 = 0,0
most = ''

for i in range(len(words)):
    num2 = paragraph.count(paragraph[i])

    if num1<num2:
        num1 = num2
        most = paragraph[i]
    

print(most)