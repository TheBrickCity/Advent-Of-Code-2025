input = open("Day-3-Puzzle-1-Input.txt", "r")
max_index = 0
highest_nums = []
for line in input:
    indexed_line = [number for number in line if number != '\n']
    for i in range(len(indexed_line)-1):
        if indexed_line[i] > indexed_line[max_index]:
            max_index = i
    max_index_2 = max_index + 1
    for i in range(max_index+1,len(indexed_line)):
        if indexed_line[i] > indexed_line[max_index_2]:
            max_index_2 = i
    highest_nums.append(int(str(indexed_line[max_index])+str(indexed_line[max_index_2])))
    max_index_2 = 0
    max_index = 0
print(sum(highest_nums))