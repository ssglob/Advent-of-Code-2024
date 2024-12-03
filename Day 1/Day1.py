# Part 1
file = open('Advent of Code 2024\\Day 1\\Day 1 input','r')
left = []
right = []
for line in file:
    a = line.split()
    left.append(int(a[0]))
    right.append(int(a[1]))
file.close()

left.sort()
right.sort()
total = 0
for count in range(len(left)):
    total += abs(left[count]-right[count])

print(total)

# Part 2
num_right = {}
for item in right:
    if item in num_right:
        num_right[item] += 1
    else:
        num_right[item] = 1

set_right = set(right)
sim_score = 0
for count in range(len(left)):
    if left[count] in set_right:
        sim_score += left[count] * num_right[left[count]]
print(sim_score)