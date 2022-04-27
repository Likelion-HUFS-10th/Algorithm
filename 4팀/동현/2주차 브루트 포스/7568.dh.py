"""
등수 -> 자신보다 더 덩치가 크다고 판단되는 사람 수
딕셔너리 -> {몸무게 : 키}
전체 인원에 대해 for 반복문을 통해 비교
"""

people_num = int(input('사람의 수를 입력하시오: '))
people = {}

for i in range(people_num):
    weight, height = map(int, input().split())
    people[weight] = height

for j in people.keys():
    result = 1
    for k in people.keys():
        if j < k:
            if people[j] < people[k]:
                result += 1
    print(result)




