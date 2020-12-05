f = open("input.txt", "r")

seats = f.read().split("\n")

#alternative method part 1
def getSeatID(seat):
    id = 0
    row = 0
    for x in range(7):
        if seat[x] == "B":
            row += 2 ** (6-x)
    id += row * 8
    col = 0
    for x in range(3):
        if seat[x+7] == "R":
            col += 2 ** (2-x)
    id += col
    return id

currMax = 0
for s in seats:
    currMax = max(currMax, getSeatID(s))


print(currMax)

#part 2
seats = [getSeatID(s) for s in seats]
seats = sorted(seats)
for x in range(currMax):
    if x in seats and not x+1 in seats:
        print(x+1)