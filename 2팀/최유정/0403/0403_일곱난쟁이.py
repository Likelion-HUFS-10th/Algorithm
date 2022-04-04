dwarf = [
    int(input())
    for _ in range(9)
]
for i in range(9):
    for j in range(i+1, 9):
        if (sum(dwarf) - (dwarf[i] + dwarf[j])) == 100:
            fake1, fake2 = dwarf[i], dwarf[j]
            dwarf.remove(fake1)
            dwarf.remove(fake2)
            dwarf.sort()

            for k in range(len(dwarf)):
                print(dwarf[k])
            break
    if len(dwarf) < 9:
        break