n = int(input())
if n <= 4: m = 5
else: m = n
num = 1
array = [1, 2, 3, 5]

while len(array) < m:
    for i in range(2, num):
        if num % i == 0 and (num // i) in array and num not in array:
            array.append(num)
            break
    num += 1
    
array = sorted(array)
print(array[n-1])