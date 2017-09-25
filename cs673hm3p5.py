sortedArray = [0, 1, 1, 2, 3, 3]
duplicateArray = {1: [1, 1], 3: [3, 3]}
N = len(sortedArray)


i = 0
while i < N:
    print(i)
    if sortedArray[i] == sortedArray[i+1]:
        element = sortedArray[i]
        originalOrder = duplicateArray[element]
        for j in range(len(originalOrder)):
            sortedArray[i] = originalOrder[j]
            i += 1
    else:
        i += 1

print(sortedArray)
