f = open("input.txt", "r")

rules = f.read().split("\n")
#part 1 (super high runtime)
"""
def canHoldGold(bag):
    inside = bag[bag.index("contain")+8:].split(", ")
    inside = [i[i.index(" ")+1:i.index("bag")-1] for i in inside]
    for bags in inside:
        if bags == "no other":
            return False
        if bags == "shiny gold":
            return True
        else:
            for r in rules:
                if bags in r[:r.index("contain")-1]:
                    if canHoldGold(r):
                        return True
    return False


count = 0
for r in rules:
    if(canHoldGold(r)):
        count+=1
print(count)
"""

#try 2 (dicts)
bagDict = {}
for r in rules:
    r = r.replace(" bags", "").replace("s ", "").replace(".", "").replace(" bag", "")
    bagDict[r[:r.index("contain")-1]] = [b[2:] for b in r[r.index("contain")+8:].split(", ")]

def canHoldGold(bag):
    if "shiny gold" in bagDict[bag]:
        return True
    if " other" in bagDict[bag]:
        return False
    else:
        for b in bagDict[bag]:
            if canHoldGold(b):
                return True
    return False
count = 0
for b in bagDict:
    if canHoldGold(b):
        count+=1
print(count)


#part 2
def countBags(bag):
    count = 0
    inside = bag[bag.index("contain")+8:].split(", ")
    inside = [i[:i.index("bag")-1] for i in inside]
    for bags in inside:
        if bags == "no other":
            return 0
        else:
            for r in rules:
                if bags[2:] in r[:r.index("contain")-1]:
                    count = count + int(bags[0]) + int(bags[0]) * countBags(r)


    return count
print(countBags("shiny gold bags contain 4 wavy green bags, 2 mirrored teal bags, 4 dark tomato bags, 2 faded beige bags."))