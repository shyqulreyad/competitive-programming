nums = [2,2,1,1,1,2,2]
nums = [3,2,3]
length = len(nums)
nums.sort()
i = 0
counter = 1
target = length/2
while i < length:
    if i+1 < length:
        if nums[i] ==nums[i+1]:
            counter+=1
            if counter > target:
                print(nums[i])
        else:
            counter = 1
    else:
        print(nums[i])
    i+=1