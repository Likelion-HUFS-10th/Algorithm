#2557_Hello World
print("Hello World!")

#10718_We love kriii
print("강한친구 대한육군 \n강한친구 대한육군")

#10171 CAT : r""" = raw string
print(r'''\    /\
 )  ( ')
(  /  )
 \(__)|'''
)

#10172 snoopdoggie : 10171과 마찬가지로 raw string 사용
print(
r'''
|\_/|
|q p|   /}
( 0 )"""\
|"^"`    |
||_/=\\__|
'''
)

#1000번 A + B : map(int, input().split())을 모르면 정답 도출 힘든 것 같다. 결과로 출력되는 것은 심플하게 만들 수 있었지만 하드코딩이 아닐까하는 생각.
'''input().split()) : 한 번에 입력 받은 여러 개의 값을 앞에 선언한 변수의 수 만큼 split해 각 변수에 assign.
* map(function, iterable) : 함수의 동작은 두 번째 인자로 들어온 반복 가능한 자료형을 첫 번째 인자로 들어온 함수에 하나씩 집어넣어서 함수를 수행하는 함수.
* 즉, map(적용시킬 함수, 적용할 값들) 이런 식.
* 재밌는 건 여기서의 int가 단순히 datatype을 알려주는 키워드인 줄 알았는데 int()였다는 점.
'''
A, B = map(int, input().split())
print(A + B)

#1001번 A - B : 위와 동일
A, B = map(int, input().split())
print(A - B)

#10998번 : A * B : 이제 그만해줘. 특이한 점은 A<0, B<10이라는 조건인데 왜 붙어있는걸까?
A, B = map(int, input().split())
print(A * B)

#1008번 : A / B : 이번엔 기존의 방법 외에 다른 방법으로도 풀어보자.
A, B = input().split()
A = int(A)
B = int(B)
print(A / B)
#일단은 통과하였으나 오차범위가 10의 -9승 이내로 나야한다는 조건에 불편함을 느낀다. 그 말은 나눗셈의 결과가 소숫점 아래 9자리보다 더 길어지거나 무한소수여야한다는 뜻.
#그렇다면 파이썬도 결과값이 조건을 만족하도록 data type handling을 해야하지 않나..?
'''
float : 32비트(4바이트) 자료형이다.
double : 64비트(8바이트) 자료형이다.
 
이 두 자료형을 각각 이렇게도 부른다.
float : 단 정밀도 (single precision)
double : 배 정밀도 (double precision)

java에서는 float : 10의 -7승 / double : 10의 -9승 이상
따라서 java 라면 double을 사용하는 게 맞음.

Python의 경우 기본 나눗셈 연산 결과 나누어떨어지지 않을 경우 소수점 아래 16자리의 실수로 출력하는 것이 Default라고 한다.
'''

#10869번 : 덧셈, 뺄셈, 곱셈 + 몫(얘 주의) + modulo(%, 나머지) 출력
A, B = map(int, input().split())
print(A + B)
print(A - B)
print(A * B)
print(int(A / B))
print(A % B)

#10926번 : String Concatenation Prob,..?
existing_id = input()
print(existing_id + "??!")

#18108번 : 불기연도 - 서기연도 = 543년차이가 난다고 함.
bg_year = int(input())
print(bg_year - 543)

#10430 : 첫째 줄에 (A+B)%C, 둘째 줄에 ((A%C) + (B%C))%C, 셋째 줄에 (A×B)%C, 넷째 줄에 ((A%C) × (B%C))%C를 출력한다.
A, B, C = map(int, input().split())
print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print(((A%C) * (B%C))%C)

#2588 : (3), (4), (5), (6)에 들어갈 숫자를 첫째 줄 ~ 넷 째 줄에 걸쳐서 출력. 이 문제는 재밌었다.
'''
ex.     4 7 2     ---- (1)
      X 3 8 5     ---- (2)
    ----------
      2 3 6 0     ---- (3)
    3 7 7 6       ---- (4)
  1 4 1 6         ---- (5)
  ------------
  1 8 1 7 2 0     ---- (6)

'''
#input()으로 처음 받으면 string타입이라는 걸 이용해 리스트로 헤쳐나가본다. 오 맞았다..!!!
a = input()
b = input()
b_lst = []
for i in range(0, 3):
    b_lst.append(b[i])

a = int(a)
b = int(b)
print(a * int(b[-1]))
print(a * int(b[-2]))
print(a * int(b[0]))
print(a * b)


## LEVEL_1 끝!