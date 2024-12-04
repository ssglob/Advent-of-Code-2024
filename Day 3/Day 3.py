f = open('Advent of Code 2024\\Day 3\\Day 3 input.txt','r')
result = 0
for line in f:
    for c,char in enumerate(line):
        if char != 'm':
            continue
        if c > len(line)-9:
            break
        if line[c:c+4] != 'mul(':
            continue
        count = c+4
        nums = []
        cur_string = ''
        while count<=len(line)-1 and line[count] in '1234567890,)' and len(cur_string)<=3:
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