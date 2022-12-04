from string import ascii_letters

with open("day3.txt") as file:
    data = [i for i in file.read().strip().split("\n")]

totalSum  = 0

for rucksack in data:
    half = len(rucksack)//2
    left = set(rucksack[:half])
    right = set(rucksack[half:])

    for priority , char in enumerate(ascii_letters):
        if char in left and char in right:
            totalSum += priority+1

print(f"the anser for part one : {totalSum}")

# ANSWER TO THE PART 2:

totalSum1 = 0
j = 3
for i in range(0, len(data), 3):
    rucksacks = data[i:j]
    j += 3
    for priority, char in  enumerate(ascii_letters):
        if char in rucksacks[0] and char in rucksacks[1] and char in rucksacks[2]:
            totalSum1 += priority + 1


print(f"the answer to the part two is : {totalSum1}")
