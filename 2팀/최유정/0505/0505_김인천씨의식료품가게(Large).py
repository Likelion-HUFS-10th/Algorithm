t = int(input())
for i in range(t):
    sale_price = []
    p = int(input())
    p_list = list(map(int, input().split()))
    while True:
        price = (p_list[0] * 4) / 3
        if price in p_list:
            sale_price.append(str(p_list.pop(0)))
            p_list.remove(price)
        if len(p_list) == 0:
            break
    print("Case #%d: %s" % (i+1, " ".join(sale_price)))
    
