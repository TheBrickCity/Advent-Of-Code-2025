input = open("Day-5-Puzzle-1-Input.txt", "r")
intervals = []
switch = False
ids_to_check = []
final_count = 0
for line in input:
    if switch == True:
        ids_to_check.append(line.strip('\n'))
    if line == '\n':
        switch = True
    if switch == False:
        intervals.append([line.split("-")[0],line.split("-")[1][:-1]])
for id in ids_to_check:
    for interval in intervals:
        if int(interval[0]) <= int(id) <= int(interval[1]):
            final_count += 1
            break
print(final_count)
