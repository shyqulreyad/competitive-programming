nums = [1,3,4,4,2]
nums.sort()
print(nums)
length = len(nums)
i = 0
while i < length:
    if i+1 <length:
        if nums[i] == nums[i+1]:
            print('duplicate',nums[i])
    i+=1