n = int(input())
preprev = 0
prev = 1
result = 0
if n == 1:
    print(prev)
elif n == 2:
    print('1')
else: 
    for _ in range(n - 1):
        result = preprev + prev
        preprev = prev
        prev = result
    print(result)