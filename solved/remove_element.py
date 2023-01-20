nums = [0,1,2,2,3,0,4,2]
val = 2
length = len(nums)
i =0
j=0
while i < length:
    if nums[i] != val:
        nums[j] = nums[i]
        j+=1
    i+=1
print(j)