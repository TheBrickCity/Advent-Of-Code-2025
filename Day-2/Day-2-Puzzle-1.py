inputs = open("Day-2-Puzzle-1-Input.txt", "r")
ranges = inputs.read().split(",")
split_ranges = []
invalid_ids = []
sum = 0
for interval in ranges:
    split_ranges.append(interval.split("-"))
for interval in split_ranges:
    for i in range(int(interval[0]), int(interval[1])):
        num_len_half = len(str(i))//2
        if str(i)[:num_len_half] == str(i)[num_len_half:]:
            invalid_ids.append(i)
for id in invalid_ids:
    sum += id
print(sum)
