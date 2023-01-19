nums = [2,0,2,1,1,0]
nums = [0,1,0,3,12]
nums = [0]

for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i] == 0:
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
print(nums)