'''
주유소 문제

- N 은 도시 수
- city_price 도시 주유소 가격
- distance 거리

+ 처음 출발할 때 자동차에 기름 넣고 출발하기
+ 제일 왼쪽 도시에서 제일 오른쪽 도시로 이동하는 최소 비용 구하기
'''

n = int(input())
distance = list(map(int,input().split()))
city_price = list(map(int,input().split()))

# distance_sum = sum(distance)

first_cost = distance[0] * city_price[0] # 맨 처음에 가야하는 최소 거리까지만 기름 넣어주기
total = first_cost                       # 총비용에 값 미리 넣어주고 시작

first_price = city_price[0]


for i in range(1,n-1):
    if first_price > city_price[i]:  # 초기 설정 값 price[0] == 5와 2, 4, 1 크기 비교
        first_price = city_price[i]  # 5말고 2, 4, 1이 더 작으면 first_price에 넣고 다시 비교
        total += distance[i] * first_price  # 더 작은 값으로 들어온 수 * 거리

    else:
        total += distance[i] * first_price   # 초기 설정 값 price[0]==5 보다 크면 전에 넣어둔 가장 작은 값 * 거리


print(total)


