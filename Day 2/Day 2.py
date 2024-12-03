f = open('Advent of Code 2024\\Day 2\\Day 2 input.txt','r')
# Part 1
total = 0
for line in f:
    cont = True
    lst = [int(i) for i in line.split()]
    dora = lst[1]-lst[0]
    if abs(dora) <= 0 or abs(dora) >= 4:
        continue
    for i in range(len(lst)-2):
        diff = (lst[i+2] - lst[i+1])
        if diff * dora <= 0:
            cont = False
            break
        if abs(diff) >= 4:
            cont = False
            break
    if not cont:
        continue
    total += 1
f.close()
# Part 2
f = open('Advent of Code 2024\\Day 2\\Day 2 input.txt','r')
def verify(a):
    dora = a[1]-a[0]
    if abs(dora) == 0 or abs(dora) >= 4:
        return False
    for i in range(len(a)-2):
        diff = (a[i+2] - a[i+1])
        if diff * dora <= 0:
            return False
        elif abs(diff) >= 4:
            return False
    return True
total1 = 0
for line in f:
    cont = True
    first = True
    lst = [int(i) for i in line.split()]
    dora = lst[1]-lst[0]
    i = 0
    if abs(dora) == 0 or abs(dora) >= 4:
        if verify([lst[n] for n in range(len(lst)) if n != i]) or verify([lst[n] for n in range(len(lst)) if n != i+1]):
            total1 += 1
        continue
    while i < len(lst)-2:
        diff = (lst[i+2] - lst[i+1])
        if diff * dora <= 0 or abs(diff) >= 4:
            v1 = verify([lst[n] for n in range(len(lst)) if n != i])
            v2 = verify([lst[n] for n in range(len(lst)) if n != i+1])
            v3 = verify([lst[n] for n in range(len(lst)) if n != i+2])
            cont = v1 or v2 or v3
            break
        i += 1
    if not cont:
        continue
    total1 += 1
f.close()
print(total)
print(total1)