input = "./input"

leftList = []
rightList = []

with open(input, "r") as file:
    lines = file.readlines()
    for line in lines:
        left, right = line.strip().split()
        leftList.append(int(left))
        rightList.append(int(right))

leftList.sort()
rightList.sort()
listDiff = []

for i in range(len(leftList)):
    listDiff.append(abs(rightList[i] - leftList[i]))

print("Sum of differences:", sum(listDiff))