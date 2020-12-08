f = open("input.txt", "r")

instructions = f.read().split("\n")
#part 1
acc = 0
index = 0
parallel = [False for x in range(len(instructions))]
while(parallel[index] != True):
    if instructions[index][:3] == "acc":
        acc += int(instructions[index][4:])
        parallel[index] = True
        index+=1
    elif instructions[index][:3] == "nop":
        parallel[index] = True
        index+=1
    elif instructions[index][:3] == "jmp":
        temp = int(instructions[index][4:])
        parallel[index] = True
        index+=temp
print(acc)

#part 2
def infLoop(instr):
    parallel = [False for x in range(len(instr))]
    index = 0
    acc = 0
    while (parallel[index] != True):
        if instr[index][:3] == "acc":
            acc += int(instr[index][4:])
            parallel[index] = True
            if index == len(parallel)-1:
                return acc
            index += 1
        elif instr[index][:3] == "nop":
            parallel[index] = True
            if index == len(parallel)-1:
                return acc
            index += 1
        elif instr[index][:3] == "jmp":
            temp = int(instr[index][4:])
            parallel[index] = True
            if index == len(parallel)-1:
                return acc
            index += temp
    return False


for x in range(len(instructions)):
    tempinstr = list(instructions)
    if instructions[x][:3] == "nop":
        tempinstr[x] = "jmp" + instructions[x][3:]
        if bool(infLoop(tempinstr)):
            print(infLoop(tempinstr))
            break
    elif instructions[x][:3] == "jmp":
        tempinstr[x] = "nop" + instructions[x][3:]
        if bool(infLoop(tempinstr)):
            print(infLoop(tempinstr))
            break
