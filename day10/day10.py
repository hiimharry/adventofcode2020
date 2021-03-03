f = open("input.txt", "r")

voltages = f.readlines()
voltages.append("0")
voltages = sorted([int(x.replace("\n","")) for x in voltages])


oneJumps = 0
threeJumps = 1
prevVoltage = 0

for v in voltages:
    if v - prevVoltage == 1:
        oneJumps+=1
    elif v - prevVoltage == 3:
        threeJumps +=1
    prevVoltage = v

print(oneJumps*threeJumps)

def isSkippable(v):
    if (v+1 in voltages and (v-2 in voltages or v-1 in voltages)) or (v+2 in voltages and v-1 in voltages):
        return True
    return False

total = 1
v = 0
while v < len(voltages):
    if(isSkippable(voltages[v])):
        if (isSkippable(voltages[v+1])):
            if (isSkippable(voltages[v+2])):
                total*=7
            else:
                total*=4
        else:
            total*=2
        v+=3
    else:
        v+=1
print(total)