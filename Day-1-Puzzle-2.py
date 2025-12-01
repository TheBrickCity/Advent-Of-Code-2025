inputs = open("Day-1-Puzzle-1-Input.txt", "r")
current_position = 50
zero_count = 0
for input in inputs:
    turn_direction = input[0]
    turn_count = int(input[1:])
    for turn in range(turn_count):
        if turn_direction == 'L':
            current_position -= 1
        elif turn_direction == 'R':
            current_position += 1
        if current_position == -1:
            current_position = 99
        elif current_position == 100:
            current_position = 0
        if current_position == 0:
            zero_count += 1
print(zero_count)
