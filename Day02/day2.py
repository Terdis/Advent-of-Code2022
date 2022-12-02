#### PART ONE

lettersMovesDict = {
    "A" : "Rock",
    "B" : "Paper",
    "C" : "Scissors",
    "X" : "Rock",
    "Y" : "Paper",
    "Z" : "Scissors"
}

wonDict = {"A" : "Z", "B" : "X", "C" : "Y"}
rewardDict = {"X" : 1, "Y" : 2, "Z" : 3, "victory" : 6, "draw" : 3, "loss" : 0}

finalScore = 0

with open("./Day02/input.txt", "r") as f:
    for line in f.read().splitlines():
        adv, me = line.split(" ")

        if (wonDict[adv] == me):
            finalScore += rewardDict["loss"]
        elif (lettersMovesDict[adv] == lettersMovesDict[me]):
            finalScore += rewardDict["draw"]
        else:
            finalScore += rewardDict["victory"]

        finalScore += rewardDict[me]

f.close()
print(f"FINAL SCORE: {finalScore}")


#### PART TWO

lettersMovesDictNew = {
    "A" : "Rock",
    "B" : "Paper",
    "C" : "Scissors",
    "X" : "loss",
    "Y" : "draw",
    "Z" : "victory"
}

rewardDictNew = {"Rock" : 1, "Paper" : 2, "Scissors" : 3, "victory" : 6, "draw" : 3, "loss" : 0}
victoryDict =  {"A" : "B", "B" : "C", "C" : "A"}

finalScore = 0

with open("./Day02/input.txt") as f:
    for line in f.read().splitlines():
        adv, move = line.split(" ")
        finalScore += rewardDictNew[lettersMovesDictNew[move]]
        if (lettersMovesDictNew[move] == "victory"):
            finalScore += rewardDictNew[lettersMovesDictNew[victoryDict[adv]]]
        elif (lettersMovesDictNew[move] == "draw"):
            finalScore += rewardDictNew[lettersMovesDictNew[adv]]
        else:
            finalScore += rewardDictNew[lettersMovesDictNew[victoryDict[victoryDict[adv]]]]

print(f"FINAL SCORE: {finalScore}")



