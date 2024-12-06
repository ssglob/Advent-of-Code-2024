# Part 1
f = open("Advent of Code 2024\Day 5\Day 5 input.txt", "r")
a = '''47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47'''
total = 0
allowed = {}
lst = []
dictis = True
for line in f:
    if line in ' \n':
        dictis = False
        continue
    if dictis:
        b = [i for i in line.strip().split('|')]
        if b[0] in allowed:
            allowed[b[0]].append(b[1])
        else:
            allowed[b[0]] = [b[1]]
    else:
        lst.append([i for i in line.strip().split(',')])
f.close()
for line in lst:
    a = True
    for num in line:
        if num in allowed:
            for num1 in allowed[num]:
                if num1 in line and line.index(num1) < line.index(num):
                    a = False
                    break
    if a:
        total += int(line[len(line)//2])
print(total)
print()

# Part 2
def verify(nums,keys):
    pass
total1 = 0
for l in lst:
    line = l[:]
    a = False
    add = 0
    done = 0
    times = 0
    while done<3 and not a:
        for num in line:
            if num in allowed:
                for num1 in allowed[num]:
                    if num1 in line and line.index(num1) < line.index(num):
                        a = False
                        n1, n2 = line.index(num),line.index(num1)
                        line[n2], line[n1] = line[n1],line[n2]
        if l == line and times == 0:
            a = True
        times += 1
        if line[len(line)//2] == add:
            done += 1
        else:
            add = line[len(line)//2]
            done = 0
    if not a:
        total1 += int(line[len(line)//2])
print(total1)