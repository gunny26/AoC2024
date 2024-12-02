#!/usr/bin/python3

filename = "first_example.txt"  # example data
filename = "first.txt"  # puzzle input

reports = [[int(entry) for entry in line.split()] for line in open(filename, "rt").read().split("\n") if line]
print(reports)
safe_reports = 0
for report in reports:
    print(report)
    steps = [report[index+1] - report[index] for index in range(len(report) - 1)]
    print(steps)
    # Any two adjacent levels differ by at least one and at most three.
    if any([abs(entry) > 3 for entry in steps]) or any([abs(entry) == 0 for entry in steps]):
        print("unsafe")
    # The levels are either all increasing or all decreasing.
    elif not( all((entry >= 0 for entry in steps)) or all((entry <= 0 for entry in steps)) ):
        print("unsafe")
    else:
        print("safe")
        safe_reports += 1
    print("-" * 80)
print("safe_reports: ", safe_reports)
