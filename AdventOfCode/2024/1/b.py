input = "./input"

leftList = []
rightDict = {}

with open(input, "r") as file:
    lines = file.readlines()
    for line in lines:
        left, right = line.strip().split()
        leftList.append(int(left))
        rightDict[int(right)] = rightDict.get(int(right), 0) + 1


similarityScores = []

for key in leftList:
    if key in rightDict:
        similarityScores.append(key * rightDict[key])

print ("Similarity scores:", similarityScores)

print("Sum of similarity:", sum(similarityScores))