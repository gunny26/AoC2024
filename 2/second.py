#!/usr/bin/python3

filename = "second_example.txt"  # example data
# filename = "second.txt"  # puzzle input

reports = [[int(entry) for entry in line.split()] for line in open(filename, "rt").read().split("\n") if line]
print(reports)
print("-" * 80)
safe_reports = 0
for report in reports:
    unsafes = 0
    print(report)
    steps = [report[index+1] - report[index] for index in range(len(report) - 1)]
    print(" ", steps)
    # Any two adjacent levels differ by at least one and at most three.
    if any([abs(entry) > 3 for entry in steps]) or any([abs(entry) == 0 for entry in steps]):
        unsafes += 1
        print("unsafe step size")
    # The levels are either all increasing or all decreasing.
    if not( all((entry >= 0 for entry in steps)) or all((entry <= 0 for entry in steps)) ):
        unsafes += 1
        print("unsafe monotony")
    else:
        if unsafes == 1:
            safe_reports += 1
            print("safe with unsafe")
        else:
            safe_reports += 1
            print("safe")
    print("-" * 80)
print("safe_reports: ", safe_reports)
