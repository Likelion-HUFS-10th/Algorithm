n = int(input())
rgb = []

for _ in range(n):
    cost = list(map(int,input().split()))
    rgb.append(cost)

for i in range(n):
    if i == 0:
        rgb[i][0] = rgb[i][0]
        rgb[i][1] = rgb[i][1]
        rgb[i][2] = rgb[i][2]
    else:
        rgb[i][0] = min(rgb[i-1][1],rgb[i-1][2]) + rgb[i][0] # 빨간색
        rgb[i][1] = min(rgb[i-1][0],rgb[i-1][2]) + rgb[i][1] # 초록색
        rgb[i][2] = min(rgb[i-1][0],rgb[i-1][1]) + rgb[i][2] # 파란색

print(min(rgb[n-1][0],rgb[n-1][1],rgb[n-1][2]))
