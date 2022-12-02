
with open("data.txt") as file:
    rounds = [i for i in file.read().strip().split("\n")]
    #print( rounds)

    outcomes = {
        "A X" :4, "A Y" :8, "A Z": 3,
        "B X": 1, "B Y": 5, "B Z": 9,
        "C X": 7, "C Y": 2, "C Z": 6
    }

    totalPoints = 0
    for round in rounds:
        totalPoints += outcomes[round]

## Answers to part 1

print("Answer for the part 1: ",totalPoints)


## part two

desired_outcomes = {
        "A X": 3, "A Y": 4, "A Z": 8,
        "B X": 1, "B Y": 5, "B Z": 9,
        "C X": 2, "C Y": 6, "C Z": 7
    }
totalPoints1 = 0
for round in rounds:
    totalPoints1 += desired_outcomes[round]

# Answer round twp :

print(f"the answer for round two is {totalPoints1}")
