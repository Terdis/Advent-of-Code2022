##### PART ONE

import string
from itertools import islice


priorityDict = dict(zip(string.ascii_lowercase + string.ascii_uppercase, range(1, 53)))
priorSum = 0
with open("./Day03/input.txt") as f:
    for line in f.readlines():
        size = len(line)
        firstItem = line[:int(size/2)]
        secondItem = line[int(size/2):]

        commonChars = list(set(firstItem)&set(secondItem))
        priorSum += sum([priorityDict[c] for c in commonChars])

f.close()
print(f"SUM OF THE PRIORITIES: {priorSum}")

##### PART TWO

priorSum = 0

with open("./Day03/input.txt") as f:
    while True:
        nextThreeGroup = list(islice(f, 3))
        if not nextThreeGroup:
            break
        
        commonChars = list(set(nextThreeGroup[0][:-1])&set(nextThreeGroup[1][:-1])&set(nextThreeGroup[2][:-1]))
        priorSum += sum([priorityDict[c] for c in commonChars])

print(f"SUM OF THE PRIORITIES: {priorSum}")
        


