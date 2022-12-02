with open ("data.txt") as file:
    data = [i for i in file.read().strip().split("\n")]

## traversing every item in the data

count = 0
max = 0
max1 = 0 #calory carried by the second elf
max2 = 0 # calory carried by the third elf

for item in data :
    if item == "":
        count = 0
    else:
        num = int(item)
        count += num
    if count > max:
        max = count
    elif count > max1:
        max1 = count
    elif count > max2:
        max2 = count

print(f"anser to part 1: {max}")
print(f"answer for part 2: {max+max1+max2}")
print(max,max1,max2, count)



