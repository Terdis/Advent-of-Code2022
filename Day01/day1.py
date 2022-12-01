##### FOR PART ONE


with open("./Day01/in.txt", "r") as f:
    maxCal=0
    elf=1
    elf_max=1
    calories=0
    for line in f.readlines():
        if (line == "\n"):
            if (calories > maxCal):
                maxCal = calories
                elf_max = elf
            elf += 1
            calories = 0
        else:
            cal = int(line)
            calories += cal

f.close()
print(f"THE WINNER IS {elf_max} WITH {maxCal} CALORIES")

##### FOR PART TWO

with open("./Day01/in.txt", "r") as f:
    elfCalories=[]
    sumCal=0
    elf=1

    for line in f.readlines():
        if (line == "\n"):
            elfCalories.append((elf, sumCal))
            sumCal = 0
            elf += 1
        else:
            cal = int(line)
            sumCal += cal

    elfCalories.sort(key = lambda a: a[1], reverse=True)
    print(f"THE TOP THREE: {elfCalories[:3]}, THE TOTAL IS: {sum([calories[1] for calories in elfCalories[:3]])}")


