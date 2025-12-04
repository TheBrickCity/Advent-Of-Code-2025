input = open("Day-4-Puzzle-1-Input.txt", "r")
layout = []
final_count = 0
def check_surrounding(input_x,input_y, layout):
    counter = 0
    for x in [-1,0,1]:
        for y in [-1,0,1]:
            if x == 0 and y == 0:
                continue
            if 0 <= input_x + x < len(layout) and 0<= input_y + y < len(layout[row]):
                if layout[input_x+x][input_y+y] == '@':
                    counter += 1
    return counter

for line in input:
    layout.append([char for char in line if char != '\n'])

while(True):
    temp_count = 0
    spaces_to_clear = []
    for row in range(len(layout)):
        for col in range(len(layout[0])):
            if layout[row][col] == '@':
                if check_surrounding(row,col,layout) < 4:
                    spaces_to_clear.append([row,col])
                    temp_count += 1
    for index in spaces_to_clear:
        layout[index[0]][index[1]] = '.'
    final_count += temp_count
    if temp_count == 0:
        break
print(final_count)
