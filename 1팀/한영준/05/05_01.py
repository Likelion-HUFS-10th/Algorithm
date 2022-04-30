hap = 0

a = [1, 2,3,4,5]

def solve (a: list) -> int :
    for i in a:
        global hap
        hap = hap +a[i-1]
    return hap


print(solve(a))