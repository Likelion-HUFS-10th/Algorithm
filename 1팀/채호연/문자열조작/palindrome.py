#1. 직접 시도.
import time
start = time.process_time()

def isPalin():
    s = input()
    s_lst = [i.lower() for i in s if ord(i) in range(65, 91) or ord(i) in range(97, 123) or ord(i) in range(48, 58)] #아스키 문자와 대조하는 방식으로 영문자 아닌 것 배제
    reversed_s_lst = list(reversed(s_lst)) #reversed() = iterator 객체의 '참조주소' 반환. => 형변환 필수.
    print(s_lst)
    print(reversed_s_lst)

    if s_lst == reversed_s_lst:
        print("True")
        return True
    else:
        print("False")
        return False
    
'''isPalin() # 성공!'''

#end = time.process_time()
#print('{:.3f}ms'.format(end-start/1000))

#2. 리스트.pop()을 이용한 방법
def isPalindrome(s: str) -> bool:
    strs = []
    for char in s:
        if char.isalnum(): #isalnum() = 영문자/숫자 판별하는 함수. 
            strs.append(char.lower())
        
    while len(strs) > 1:
        if strs.pop(0) != strs.pop(): #순서를 굳이 뒤집지 않고 맨 첫 글자와 마지막 글자를 뽑아 비교하는 방식.
            return False
    
    return True

isPalindrome('Palindrome')

#3. 데크 자료형을 이용한 최적화
'''
데크(Deque) : 보통 큐는 선입선출(FIFO) 방식으로 작동한다. 그러나 데크는 양방향 큐 이다.
즉, 앞, 뒤 양방향에서 element를 추가하거나 삭제할 수 있다.
결국 양쪽 끝을 모두 추출할 수 있는, 큐를 일반화한 형태의 추상 자료형(ADT)이다.
'''
def isPalindrome(s: str) -> bool:
    import collections
    strs = collections.deque()

    for char in s:
        if char.isalnum():
                    strs.append(char.lower())
        
    while len(strs) > 1:
        if strs.popleft() != strs.pop(): #순서를 굳이 뒤집지 않고 맨 첫 글자와 마지막 글자를 뽑아 비교하는 방식.
            return False
    
    return True

isPalindrome('anam')

#3. 슬라이싱 사용
import re
def isPalindrome(s:str) -> bool:
    s = s.lower()
    s = re.sub('[^a-z0-9]', '', s)
    '''
    re.() => import re 해야 사용 가능

    * 정규 표현식 : 텍스트에서 특정 문자열을 찾기 쉽도록 고안된 문자열 탐색 방법 

    1. 정규표현식 기호 정리
    https://hamait.tistory.com/m/342

    '''
    return s == s[::-1]