f = open("input.txt", "r")

slopes = list(f.readlines())

slopes = [x.strip() for x in slopes]

#day1
def treesOnSlope(x, y):
    trees = 0
    currRow = 0
    for k in range(y, len(slopes), y):
        currRow = currRow + x
        if slopes[k][currRow % len(slopes[k])] == "#":
            trees = trees + 1
    return trees

print(treesOnSlope(3, 1))

#day2
print(treesOnSlope(1,1) * treesOnSlope(3,1) * treesOnSlope(5,1) * treesOnSlope(7,1) * treesOnSlope(1,2))