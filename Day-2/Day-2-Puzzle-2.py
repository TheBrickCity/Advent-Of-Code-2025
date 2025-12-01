inputs = open("Day-2-Puzzle-1-Input.txt", "r")
ranges = inputs.read().split(",")
split_ranges = []
invalid_ids = []
sum = 0
for interval in ranges:
    split_ranges.append(interval.split("-"))
for interval in split_ranges:
    for i in range(int(interval[0]), int(interval[1])):
        s = str(i)
        possible_repeats = [int(s[:i]) for i in range(1, len(s)+1) if i <= len(s)/2]
        for possible in possible_repeats:
            to_check = ""
            while len(to_check) < len(s):
                to_check += str(possible)
            if s == to_check:
                invalid_ids.append(i)
                break
for id in invalid_ids:
    sum += id
print(sum)


