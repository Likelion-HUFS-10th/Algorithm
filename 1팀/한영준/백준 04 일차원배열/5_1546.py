n = int(input())
jumsoo = list(map(int, input().split()))
max = 0
new_jumsoo = 0

for i in range(n):
    if jumsoo[i] > max :
        max = jumsoo[i]

for i in range(n):
    new_jumsoo += jumsoo[i]/max*100

print(new_jumsoo/n)