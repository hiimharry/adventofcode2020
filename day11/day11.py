f = open("input.txt", "r")

seating = f.readlines()
seating = [x.replace("\n", "") for x in seating]
seats = []
for rows in seating:
    seats.append(list(rows))

def iterate():
    temp = []
    for rows in seats:
        temp.append(rows.copy())
    for x in range(len(seats)):
        for y in range(len(seats[x])):
            if seats[x][y] == "L":
                if checkAdjacent(x, y) == 0:
                    temp[x][y] = "#"
            elif seats[x][y] == "#":
                if checkAdjacent(x, y) >= 4:
                    temp[x][y] = "L"
    return temp


def checkAdjacent(x, y):
    count = 0
    try:
        if seats[x][y + 1] == "#":
            count += 1
    except IndexError:
        pass
    if seats[x][y - 1] == "#" and y-1 >= 0:
        count += 1
    try:
        if seats[x + 1][y + 1] == "#":
            count += 1
    except IndexError:
        pass
    try:
        if seats[x + 1][y] == "#":
            count += 1
    except IndexError:
        pass
    try:
        if seats[x + 1][y - 1] == "#" and y-1 >= 0:
            count += 1
    except IndexError:
        pass
    try:
        if seats[x - 1][y + 1] == "#" and x-1 >= 0:
            count += 1
    except IndexError:
        pass
    if seats[x - 1][y] == "#" and x-1 >= 0:
        count += 1
    if seats[x - 1][y - 1] == "#" and x-1 >= 0 and y-1 >= 0:
        count += 1

    return count

while(seats != iterate()):
    seats = iterate()
occupied = 0
for x in range(len(seats)):
    for y in range(len(seats[x])):
        if seats[x][y] == "#":
            occupied+=1
print(occupied)

def checkAdjacentv2(x, y):
    count = 0
    while()