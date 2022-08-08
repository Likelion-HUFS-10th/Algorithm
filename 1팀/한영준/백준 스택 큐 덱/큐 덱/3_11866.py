from collections import deque

people = deque()
n,k = map(int, input().split())
cnt = 1
jose = []

for i in range(n):
    people.append(i+1)
    
while len(people) !=0 :
    if cnt == k:
        jose.append(people[0])
        people.popleft()
        cnt = 1
    else :
        people.append(people[0])
        people.popleft()
        cnt +=1

print(jose)
    

