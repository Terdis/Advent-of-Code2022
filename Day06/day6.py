#### PART ONE


with open("./Day06/input.txt") as f:
    line = f.read()
    n = 4

    for i in range(len(line)):
        substr = line[i:i+n]
        if (len(substr) == len(set(substr))):
            print(f"START OF PACKET MARKER: {i+n}, {substr}")
            break

f.close()

##### PART TWO

with open("./Day06/input.txt") as f:
    line = f.read()
    n = 14

    for i in range(len(line)):
        substr = line[i:i+n]
        if (len(substr) == len(set(substr))):
            print(f"START OF PACKET MARKER: {i+n}, {substr}")
            break

f.close()
