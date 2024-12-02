#!/usr/bin/python3

# data = open("second_example.txt", "rt").read().split("\n")
data = open("second.txt", "rt").read().split("\n")
left = [int(line.split()[0]) for line in data if line]
print("left: ", left)
right = sorted([int(line.split()[1]) for line in data if line])
print("right: ", right)
assert len(left) == len(right)
appearances = [entry * right.count(entry) for entry in left]
print(appearances)
similarity_score = sum(appearances)
print(similarity_score)
