"""
리스트로 split해서 받았을 때의 해결을 못함..
그냥 문장으로 받아도 된다는 점을 생각 못함
"""
s = list(input())

flag = True
word = ''
result = ''

for w in s:
    if flag:
        if w == '<':
            flag = False
            word = word + w
        elif w == ' ':
            word = word + w
            result = result + word
            word = ''
        else:
            word = w + word
            
    elif flag == False:
        word = word + w
        if w == '>':
            flag = True
            result = result +  word
            word = ''

result_sent = result + word
print(result_sent)