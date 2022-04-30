#4344(평균)
n = int(input())

for _ in range(n):
    nums = list(map(int, input().split()))
    avg = sum(nums[1:])/nums[0]  # 평균을 구함 (nums[0]: 학생수, nums[1:] 점수)

    cnt = 0
    for score in nums[1:]:
        if score > avg:
            cnt += 1  # 평균 이상인 학생 수

    rate = cnt/nums[0] *100
    print(f'{rate:.3f}%')




#2562(append)
num_list = []
for i in range(9):
    num_list.append(int(input()))
    
print(max(num_list))
print(num_list.index(max(num_list))+1)




#3052(set으로 중복제거)
arr = []
for i in range(10):
    n = int(input())
    arr.append(n % 42)
arr = set(arr)
print(len(arr))




#질문1
n=int(input())
a=list(map(int, input().split()))
m=max(a)

i=0
b=[]   #for문에 넣으면 for문 안에서만 기능하나?
for i in a:
    b.append(i/m*100)
    result=sum(b)
print(result/len(a))




#질문2_1065(한수)
num = int(input())

hansu = 0
for i in range(1, num+1):
    num_list = list(map(int, str(i)))
    if i < 100:
        hansu += 1  # 100보다 작으면 모두 한수
    elif num_list[0]-num_list[1] == num_list[1]-num_list[2]:   #이게..리스트가 어찌된걸
        hansu += 1  
print(hansu)




#질문3_1110
N=int(input())
i=0
num=N
while True:
    a=N//10
    b=N%10
    c=(a+b)%10
    num=(b*10)+c
    
    i=i+1
    if num==N:
        break
print(i)

#---------
num = int(input())
check = num
new_num = 0
temp = 0
count = 0
while True:
    temp = num//10 + num%10
    new_num = (num%10)*10 + temp%10
    count += 1
    num = new_num
    if new_num == check:
        break
print(count)

