'''
1. 빅오 표기법과 자료형에 관한 다음 설명 중 틀린 것은?

2번 : 처리 시간을 입력 크기에 대한 함수로 표현한다.
'''

#2번.
def vowel_distinguisher():
    word = input("단어 입력하세요: ")
    word_lst = [i for i in word]
    vowels = ['a', 'e', 'i', 'o', 'u']
    word_dct = dict()
    
    for i in word_lst:
        result = [word_dct["{}".format(i)] = '모음' if i in vowels else word_dct["{}".format(i)] = '자음']

    return print(result)

vowel_distinguisher()