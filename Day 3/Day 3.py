# Part 1
f = open('Advent of Code 2024\\Day 3\\Day 3 input.txt','r')
result = 0
for line in f:
    for c,char in enumerate(line):
        if char != 'm':
            continue
        if c > len(line)-8:
            break
        if line[c:c+4] != 'mul(':
            continue
        count = c+4
        nums = []
        cur_string = ''
        while count<=len(line)-1 and len(cur_string)<=3:
            if not line[count] in '1234567890,)':
                nums.clear()
                break
            if line[count] == ',':
                nums.append(int(cur_string))
                cur_string = ''
            elif line[count] == ')':
                nums.append(int(cur_string))
                break
            else:
                cur_string += line[count]
            count += 1
        if len(nums) == 2:
            result += nums[0] * nums[1]
print(result)
f.close()

#Part 2
f = open('Advent of Code 2024\\Day 3\\Day 3 input.txt','r')
result = 0
do = True
for line in f:
    for c,char in enumerate(line):
        if char == 'd':
            if c < len(line)-5 and line[c:c+4] == 'do()':
                do = True
            if c < len(line)-8 and line[c:c+7] == 'don\'t()':
                do = False
        if do:
            if char != 'm':
                continue
            if c > len(line)-8:
                break
            if line[c:c+4] != 'mul(':
                continue
            count = c+4
            nums = []
            cur_string = ''
            while count<=len(line)-1 and len(cur_string)<=3:
                if not line[count] in '1234567890,)':
                    nums.clear()
                    break
                if line[count] == ',':
                    nums.append(int(cur_string))
                    cur_string = ''
                elif line[count] == ')':
                    nums.append(int(cur_string))
                    break
                else:
                    cur_string += line[count]
                count += 1
            if len(nums) == 2:
                result += nums[0] * nums[1]
print(result)
f.close()