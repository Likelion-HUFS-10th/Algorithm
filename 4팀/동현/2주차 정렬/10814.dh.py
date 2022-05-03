n = int(input()) 
people_list = []
for i in range(n):
    people_list.append(input().split())

people_list.sort(key = lambda x : x[0]) # key가 여러개 일때 사용하는 방법

for people in people_list:
    print(people[0], people[1])