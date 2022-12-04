##### PART ONE

with open("./Day04/input.txt", "r") as f:

    result = 0
    for line in f.read().splitlines():
        elf1, elf2 = line.split(",")
        sec1 = list(range(int(elf1.split("-")[0]), int(elf1.split("-")[1])+1))
        sec2 = list(range(int(elf2.split("-")[0]), int(elf2.split("-")[1])+1))

        if (all(sett in sec1 for sett in sec2) or all(sett in sec2 for sett in sec1)):
            result += 1

f.close()
print(f"SOLUTION: {result}")



##### PART TWO

with open("./Day04/input.txt", "r") as f:

    result = 0
    for line in f.read().splitlines():
        elf1, elf2 = line.split(",")
        sec1 = list(range(int(elf1.split("-")[0]), int(elf1.split("-")[1])+1))
        sec2 = list(range(int(elf2.split("-")[0]), int(elf2.split("-")[1])+1))

        if (any(sett in sec1 for sett in sec2) or any(sett in sec2 for sett in sec1)):
            result += 1

f.close()
print(f"SOLUTION: {result}")