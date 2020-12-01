f = open("input.txt", "r")

nums = []

for lines in f:
    lines = lines.replace("\n", "")
    nums.append(int(lines))
n = len(nums)

#part 1
for x in range(n):
   for y in range(x+1, n):
        if nums[x] + nums[y] == 2020:
            print("1.", nums[x] * nums[y])

            #part 2
        for z in range(y+1, n):
            if nums[x] + nums[y] + nums[z] == 2020:
                print("2.", nums[x] * nums[y] * nums[z])