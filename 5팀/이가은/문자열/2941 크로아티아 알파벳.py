x = input()
y = len(x)
cro_al = ['c=','c-','dz=','d-','lj','nj','s=','z=']
for i in range(0, len(x)):
    if len(x) < 2:
        y = len(x)
    elif len(x) == 2:
        if (x[i-2] + x[i-1]) in cro_al:
            y = 1
    elif (x[i-3]+x[i-2]+x[i-1]) in cro_al:
        y -= 2
    elif (x[i-2] + x[i-1]) in cro_al:
        y -= 1
print(y)
