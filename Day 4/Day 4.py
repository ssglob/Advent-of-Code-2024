# Part 1
f = open('Advent of code 2024\\Advent-of-Code-2024\\Day 4\\Day 4 input.txt','r')
matrix = [list(i.strip()) for i in f]
f.close()
total = 0
x = 0
y = 0
while y<=len(matrix)-1:
    if matrix[y][x] == 'X':
        #horizontal + vertical
        if x>=3 and ''.join(matrix[y][x-3:x+1]) == 'SAMX':
            total += 1
        if x<=len(matrix[y])-4 and ''.join(matrix[y][x:x+4]) == 'XMAS':
            total += 1
        if y>=3 and ''.join([i[x] for i in matrix[y-3:y+1]]) == 'SAMX':
            total += 1
        if y<=len(matrix)-4 and ''.join([i[x] for i in matrix[y:y+4]]) == 'XMAS':
            total += 1
        #diagonals
        if x>=3 and y>=3:
            cur_x = x//1
            cur_y = y//1
            string = ''
            while len(string)<4:
                string += matrix[cur_y][cur_x]
                cur_x -= 1
                cur_y -= 1
            if string == 'XMAS':
                total += 1
        if x<=len(matrix[y])-4 and y>=3:
            cur_x = x//1
            cur_y = y//1
            string = ''
            while len(string)<4:
                string += matrix[cur_y][cur_x]
                cur_x += 1
                cur_y -= 1
            if string == 'XMAS':
                total += 1
        if x>=3 and y<=len(matrix)-4:
            cur_x = x//1
            cur_y = y//1
            string = ''
            while len(string)<4:
                string += matrix[cur_y][cur_x]
                cur_x -= 1
                cur_y += 1
            if string == 'XMAS':
                total += 1
        if x<=len(matrix[y])-4 and y<=len(matrix)-4:
            cur_x = x//1
            cur_y = y//1
            string = ''
            while len(string)<4:
                string += matrix[cur_y][cur_x]
                cur_x += 1
                cur_y += 1
            if string == 'XMAS':
                total += 1
    x += 1
    if x == len(matrix[y]):
        x = 0
        y += 1
print(total)

#Part 2
total1 = 0
x = 0
y = 0
visited = {}
while y<len(matrix):
    if matrix[y][x] == 'M':
        if x>=2 and y >= 2:
            cur_x = x//1
            cur_y = y//1
            cur_x1 = x//1
            cur_y1 = y-2
            string = ''
            string1 = ''
            while len(string)<3:
                if (cur_x1,cur_y1) in visited:
                    break
                string += matrix[cur_y][cur_x]
                string1 += matrix[cur_y1][cur_x1]
                cur_x -= 1
                cur_y -= 1
                cur_y1 += 1
                cur_x1 -= 1
            if string == 'MAS' and string1 in ['MAS','SAM']:
                total1 += 1
        if x<=len(matrix[y])-3 and y >= 2:
            cur_x = x//1
            cur_y = y//1
            cur_x1 = x//1
            cur_y1 = y-2
            string = ''
            string1 = ''
            while len(string)<3:
                if (cur_x1,cur_y1) in visited:
                    break
                string += matrix[cur_y][cur_x]
                string1 += matrix[cur_y1][cur_x1]
                cur_x += 1
                cur_y -= 1
                cur_y1 += 1
                cur_x1 += 1
            if string == 'MAS' and string1 in ['MAS','SAM']:
                total1 += 1
        if x>=2 and y<=len(matrix)-3:
            cur_x = x//1
            cur_y = y//1
            cur_x1 = x//1
            cur_y1 = y+2
            string = ''
            string1 = ''
            while len(string)<3:
                if (cur_x1,cur_y1) in visited:
                    break
                string += matrix[cur_y][cur_x]
                string1 += matrix[cur_y1][cur_x1]
                cur_x -= 1
                cur_y += 1
                cur_y1 -= 1
                cur_x1 -= 1
            if string == 'MAS' and string1 in ['MAS','SAM']:
                total1 += 1
        if x<=len(matrix)-3 and y <= len(matrix)-3:
            cur_x = x//1
            cur_y = y//1
            cur_x1 = x//1
            cur_y1 = y+2
            string = ''
            string1 = ''
            while len(string)<3:
                if (cur_x1,cur_y1) in visited:
                    break
                string += matrix[cur_y][cur_x]
                string1 += matrix[cur_y1][cur_x1]
                cur_x += 1
                cur_y += 1
                cur_y1 -= 1
                cur_x1 += 1
            if string == 'MAS' and string1 in ['MAS','SAM']:
                total1 += 1
        visited[(x,y)] = 0
    x += 1
    if x == len(matrix[y]):
        x = 0
        y += 1
print(total1)