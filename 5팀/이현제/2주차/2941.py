a = list(input())
a.append(0)
pt = 0
cnt = 0
length = len(a)
while pt + 1 <= length:
    if a[pt] == 'd' and a[pt + 1] == 'z' and a[pt + 2] == '=':
        cnt += 1
        pt += 3
    elif a[pt] == 'c' and a[pt + 1] == '=':
        cnt += 1
        pt += 2
    elif a[pt] == 'c' and a[pt + 1] == '-':
        cnt += 1
        pt += 2
    elif a[pt] == 'd' and a[pt + 1] == '-':
        cnt += 1
        pt += 2
    elif a[pt] == 'l' and a[pt + 1] == 'j':
        cnt += 1
        pt += 2
    elif a[pt] == 'n' and a[pt + 1] == 'j':
        cnt += 1
        pt += 2
    elif a[pt] == 's' and a[pt + 1] == '=':
        cnt += 1
        pt += 2
    elif a[pt] == 'z' and a[pt + 1] == '=':
        cnt += 1
        pt += 2
    else:
        if a[pt] == 0:
            break
        cnt += 1
        pt += 1
print(cnt)


    