input = open("Day-5-Puzzle-1-Input.txt", "r")
intervals = []
final_count = 0
for line in input:
    if line == '\n':
        break
    intervals.append([int(line.split("-")[0]),int(line.split("-")[1][:-1])])
while(True):
    new_intervals = []
    end = False
    for i in range(len(intervals)):
        if end == True:
            break
        for g in range(len(intervals)):
            if end == True:
                break
            if i == g:
                continue
            if intervals[g][0] <= intervals[i][0] <= intervals[g][1] or intervals[g][0] <= intervals[i][1] <= intervals[g][1]\
                    or intervals[i][0]<= intervals[g][0]<=intervals[i][1] or intervals[i][0]<= intervals[g][1]<=intervals[i][1]:
                new_intervals.append([min(intervals[g][0],intervals[i][0]),max(intervals[g][1],intervals[i][1])])
                if i > g:
                    del intervals[i]
                    del intervals[g]
                else:
                    del intervals[g]
                    del intervals[i]
                end = True
    for interval in new_intervals:
        intervals.append(interval)
    if end == False:
        break
for interval in intervals:
    final_count += interval[1] - interval[0] + 1
print(final_count)
