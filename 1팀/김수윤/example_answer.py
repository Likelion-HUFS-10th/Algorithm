num= int(input("아샷추를 일주일 중 몇 번 드시겠습니까?"))

i=0
a=[]
while num<0 or num>8:
    print('그렇게는 못먹어요')
    continue
else:
    for i in range(1,num+1):
        a.append(int(input('먹을 아샷추의 개수를 입력하세요: ')))
    result=sum(a)
    print(result)
    if result>10:
        print('우웩 배가 아파요')
    else:
        print('내일 또먹어야지')

a.append('배부르다')
print(a)
