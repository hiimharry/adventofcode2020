f = open("input.txt", "r")

passwords = []
count = 0

for lines in f:
    lines = lines.replace("\n", "")
    passwords.append(lines)


# part 1
def count_letters(str, a):
    counter = 0
    for letters in str:
        if letters == a:
            counter = counter + 1
    return counter


for passes in passwords:
    realpass = passes[passes.index(":")+2:]
    lettercount = count_letters(realpass, passes[passes.index(":") - 1])
    if int(passes[0: passes.index("-")]) <= lettercount <= int(passes[passes.index("-") + 1: passes.index(":") - 2]):
        count = count + 1
print(count)

count = 0
#part 2
for passes in passwords:
    realpass = passes[passes.index(":")+2:]
    if bool(realpass[int(passes[0: passes.index("-")])-1] == passes[passes.index(":") - 1]) != \
            bool(realpass[int(passes[passes.index("-") + 1: passes.index(":") - 2])-1] == passes[passes.index(":") - 1]):
        count = count + 1
print(count)