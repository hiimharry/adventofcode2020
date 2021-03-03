f = open("input.txt", "r")

nums = f.readlines()
nums = [int(x.replace("\n","")) for x in nums]
for i in range(25, len(nums)):
    found = False
    for j in range(i-25, i):
        for k in range(j+1, i):
            if nums[j] + nums[k] == nums[i]:
                found = True
                break
        if found:
            break
    if not found:
        oddity = (nums[i])
        print(nums[i])

for i in range(len(nums)):
    currSum = nums[i]
    smallest = nums[i]
    largest = nums[i]
    for j in range(i+1, len(nums)):
        currSum += nums[j]
        if nums[j] > largest:
            largest = nums[j]
        if nums[j] < smallest:
            smallest = nums[j]
        if currSum == oddity:
            print(smallest + largest)
        elif currSum > oddity:
            break
