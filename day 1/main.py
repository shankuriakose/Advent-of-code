with open ("data.txt") as file:
    data = [i for i in file.read().strip().split("\n")]

## traversing every item in the data

load = 0
listOfloads = []


for item in data :
    if item == "":
        listOfloads.append(load)
        load = 0
    else:
        num = int(item)
        load += num

listOfloads.sort(reverse=True)

print(f"anser to part 1: {listOfloads[0]}")
print(f"answer for part 2: {listOfloads[0]+listOfloads[1]+listOfloads[2]}")



