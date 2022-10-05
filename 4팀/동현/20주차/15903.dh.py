import copy
n,m = map(int,input().split())

card_list = list(map(int,input().split()))

def two_card(card_list):
    temp_list = copy.deepcopy(card_list)
    a = min(card_list)
    temp_list.remove(a)
    b = min(temp_list)
    return a,b

for i in range(m):
    a,b = two_card(card_list)
    # print(card_list)
    sum_num = a + b
    a_index = card_list.index(a)
    card_list[a_index] = sum_num
    b_index = card_list.index(b)
    card_list[b_index] = sum_num
    # print(card_list)

print(sum(card_list))