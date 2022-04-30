#15596 : 정수 N개의 합을 출력하는 함수
def solve(a):
    return sum(a)

#4573 : 셀프넘버 출력 함수
'''
첫 번 째 접근 : 대실패 (너무 얄팍하게 접근)
def selnum():
    strt = 1
    diff = 0
    selfnumber = 0
    while selfnumber <= 10000:
        selfnumber = strt + diff
        print(selfnumber)
        strt = selfnumber

        if selfnumber < 9:
            diff = 2
        else:
            diff = 11
'''
'''두번째 접근 : 1~10000까지의 수 리스트 중 생성자가 있는 수가 아니면 출력'''
def notselfnum():
    num = num + sum(map(int, str(num)))
    return num
Notselfnum = []
for p in range(1, 10001):
    Notselfnum.append(notselfnum(p))

for q in range(1, 10001):
    if q not in Notselfnum:
        print(q)

#1065 : 한수 출력 함수 : 미결
