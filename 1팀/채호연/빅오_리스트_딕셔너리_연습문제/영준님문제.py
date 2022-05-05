'''
1번. 빅오 표기법에 따라 시간 복잡도가 낮은 순서로 나열하시오.
1) 스택의 push/pop (O(1))
2) 이진 탐색 알고리즘
3) 퀵정렬
4) 입력된 원소로 만들 수 있는 모든 순열
5) 버블 정렬
'''
#2번.
animal = {"닭":"병아리",
          "개":"강아지",
          "곰":"능소니",
          "고등어":"고도리",
          "명태":"노가리",
          "말":"망아지",
          "호랑이":"개호주"}

while True:
    animal_parents = input("{} 중 새끼 이름을 알고싶은 동물은? " .format(list(animal.keys())))
    
    if animal_parents == '끝':
        break
    else:
        print(animal.get(animal_parents, "확인 후 다시 입력해주세요."))

    
    

