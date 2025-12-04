input = open("Day-3-Puzzle-1-Input.txt", "r")
highest_nums = []
for line in input:
    starting_index = 0
    indexed_line = [number for number in line if number != '\n']
    highest_index = 0
    current_num = []
    for g in range(11,-1,-1):
        for index in range(starting_index, len(indexed_line)-g):
            if indexed_line[index] > indexed_line[highest_index]:
                highest_index = index
        current_num.append(indexed_line[highest_index])
        starting_index = highest_index + 1
        highest_index += 1
    highest_nums.append(int("".join(current_num)))
print(sum(highest_nums))



