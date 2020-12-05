import math

f = open("input.txt", "r")

seats = f.read().split("\n")

#part 2
def getSeatID(seat):
    id = 0
    upperBound = 127
    lowerBound = 0
    for x in range(7):
        if seat[x] == "F":
            upperBound -= math.ceil((upperBound-lowerBound)/2)
        if seat[x] == "B":
            lowerBound += math.ceil((upperBound-lowerBound)/2)
    id += upperBound * 8
    upperBound = 7
    lowerBound = 0
    for x in range(7, 10):
        if seat[x] == "L":
            upperBound -= math.ceil((upperBound-lowerBound)/2)
        if seat[x] == "R":
            lowerBound += math.ceil((upperBound-lowerBound)/2)
    id += upperBound
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