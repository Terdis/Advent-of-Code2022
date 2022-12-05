import re
##### PART ONE

ships = [[] for _ in range(0, 9)]


with open("./Day05/input.txt", "r") as f:
    
    rows = f.readlines()

    for i in range(0, 8):
        line = rows[i][:-1]

        print(line)
        for i in range(0, len(line), 4):
            index = int(i/4)
            if(re.match(r"^\[", line[i:i+4])):
                ships[index].append(re.sub(r"\[|\]|\s+", "", line[i:i+4]))


    [ships[i].reverse() for i in range(len(ships))]

    for row in rows[10:]:
        _, howmany, _, fr, _, to = row.split(" ")
        
        howmany = int(howmany)
        fr = int(fr)
        to = int(to)

        fr_list = [ships[fr-1].pop() for _ in range(howmany)]
        fr_list.reverse()

        for _ in range(len(fr_list)):
            el = fr_list.pop()
            ships[to-1].append(el)


f.close()


print([ships[i].pop() for i in range(len(ships))])


