# T = [73,74,75,71,69,72,76,73]
# day = 0
# days = []

# for i in range(len(T)-1) :
#     if T[i] < T[i+1] :
#         days.append(1)
#     else : #내일이 더 따숩지 않을 때
#         for j in range(i+1,len(T)):
#             if T[i] < T[j]:
#                 days.append(j-i)
                
#             else: 
#                 day+=1
            
#             if day == i-len(T):
#                 days.append(0)
#                 day = 0

# print(days)

T = [73,74,75,71,69,72,76,73]
day = 0
days = []

for i in range(len(T)-1) :
    if T[i] < T[i+1] :
        days.append(1)
    else : #내일이 더 따숩지 않을 때
        for j in range(i+1,len(T)):
            if T[i] < T[j]:
                days.append(j-i)
                break
                
            else: 
                day+=1
            
            if day == i-len(T):
                days.append(0)
                day = 0

print(days)
