nums = [1,2,3,4]
i = 0 
total = 0
length = len(nums)
while i < length:
    total+=nums[i]
    nums[i] = total
    i+=1
print(nums)