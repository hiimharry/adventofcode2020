import string
f = open("input.txt", "r")

passports = f.read().split("\n\n")
passports = [x.replace("\n", " ") for x in passports]

#part1
def validPassport1(passport):
    features = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    attributes = passport.split()
    for x in range(len(features)):
        if not (features[x] in passport):
            return False
    return True

count = 0
for p in passports:
    if validPassport1(p):
        count += 1
print(count)

#part2
def validPassport2(passport):
    features = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    attributes = passport.split()
    for x in range(len(features)):
        if not (features[x] in passport):
            return False
        else:
            for a in attributes:
                if features[x] in a:
                    features[x] = a
    for x in range(len(features)):
        if x == 0:
            if 2002 < int(features[x][4:]) or int(features[x][4:]) < 1920:
                return False
        if x == 1:
            if 2020 < int(features[x][4:]) or int(features[x][4:]) < 2010:
                return False
        if x == 2:
            if 2030 < int(features[x][4:]) or int(features[x][4:]) < 2020:
                return False
        if x == 3:
            if features[x][-2:] != "cm" and features[x][-2:] != "in":
                return False
            if features[x][-2:] == "cm":
                if 193 < int(features[x][4:-2]) or int(features[x][4:-2]) < 150:
                    return False
            else:
                if 76 < int(features[x][4:-2]) or int(features[x][4:-2]) < 59:
                    return False
        if x == 4:
            if len(features[x][5:]) != 6 or [ele for ele in list(string.ascii_lowercase[6:]) if(ele in features[x][5:])] :
                return False
        if x == 5:
            eyeclr = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
            if not any(ele in features[x] for ele in eyeclr):
                return False
        if x == 6:
            if len(features[x][4:]) != 9 or not features[x][4:].isnumeric():
                return False

    return True

count = 0
for p in passports:
    if validPassport2(p):
        count += 1
print(count)
