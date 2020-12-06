import string

f = open("input.txt", "r")

answers = f.read().split("\n\n")

#part 1
def uniqueLetters(answer):
    count = 0
    for x in string.ascii_lowercase:
        if x in answer:
            count += 1
    return count


sum = 0
for a in answers:
    sum += uniqueLetters(a)
print(sum)

#part 2
def allYes(answer):
    count = 0
    group = answer.split("\n")
    for x in string.ascii_lowercase:
        all = 0
        for g in group:
            if x in g:
                all += 1
        if all == len(group):
            count += 1
    return count

sum = 0

for a in answers:
    sum += allYes(a)
print(sum)