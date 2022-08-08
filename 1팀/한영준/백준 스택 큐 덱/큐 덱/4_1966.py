from collections import deque

t= int(input())
soonseo = []
max = 0

for _ in range(t):
    n,m = map(int, input().split())
    moonseo = deque(map(int, input().split()))  
    m = moonseo[m]
    while len(moonseo) != 0 :
        max = moonseo[0]
        for j in range(len(moonseo)):
            if moonseo[0] < moonseo[j]:
                max = moonseo[j]
        if max == moonseo[0]:
            soonseo.append(moonseo[0])
            moonseo.popleft()
        else :
            moonseo.append(moonseo[0])
            moonseo.popleft()
            
    print(soonseo.index(m)+1)
    soonseo = []

    #중복 못거름


















# set = int(input())

# soonseo = 1 #n번째
# num = 0 #크기 비교용

# for k in range(set):
#     n,m = map(int, input().split())
#     #m은 인덱스값
#     moonseo = list(map(int, input().split()))
#     for i in range(len(moonseo)-1):
#         for j in range(1,len(moonseo)):
#             if moonseo[i] < moonseo[j]:
#                 num = 1
#         if num == 1:
#             moonseo.append(moonseo[0])
#             moonseo.remove(moonseo[0])
#             soonseo += 1
#             print(soonseo)
#         else :
#             moonseo.remove[0]
#             print(soonseo)


