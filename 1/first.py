#!/usr/bin/python3

# data = open("first_example.txt", "rt").read().split("\n")
data = open("first.txt", "rt").read().split("\n")
left = sorted([int(line.split()[0]) for line in data if line])
print(left)
right = sorted([int(line.split()[1]) for line in data if line])
print(right)
assert len(left) == len(right)
distances = [abs(left_entry - right_entry) for left_entry, right_entry in zip(left, right)]
print(distances)
distance = sum(distances)
print(distance)
