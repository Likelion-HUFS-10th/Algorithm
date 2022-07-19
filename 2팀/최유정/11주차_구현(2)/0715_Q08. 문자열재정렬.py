sen = list(input())
sen.sort()
num = 0

while True:
    s = sen[0]
    if s <= '9':
        num += int(s)
        sen.pop(0)
    else:
        break
str = "".join(sen) + str(num)
print(str)