#유효한 팰린드롬_주어진 문자열이 팰린드롬인지 확인하라. 대소문자를 구분하지 않으며, 영문자와 숫자만을 대상으로 한다.
str= str(input())
str= str.lower()
str2=str[::-1]
list1=[]
list2=[]
for letter in str:
    list1.append(letter)
for letter2 in str2:
    list2.append(letter2)

if list1==list2:
    print("true")
else:
    print("false")



#문자열 뒤집기_ 문자열을 뒤집는 함수를 작성하라. 입력값은 문자배열이며, 리턴없이 리스트 내부를 직접 조작하라. 
str= input().split()
str=str[::-1]
print(str)