"""
가격이 가장 저렴한 주유소를 만나기 전에는 그래도 최소한의 값으로 넣어야함
최소한의 값 변경해가며 해결
인덱스로는 복잡..?? 해결 불가
"""
N = int(input())

road_list = list(map(int,input().split()))
city_list = list(map(int,input().split()))

result = 0

# min_price = min(city_list)
# min_index = city_list.index(min_price)

cost = city_list[0]

for i in range(N-1):
    if city_list[i] < cost:
        cost = city_list[i]
    result += cost * road_list[i]

print(result)