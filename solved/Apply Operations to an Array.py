nums = [1,2,2,1,1,0]
nums = [0,1]
length = len(nums)
counter = 0
i=0
while i < length:
    if i+1 < length:
        if nums[i] == nums[i+1]:
            nums[i] =nums[i]*2
            nums[i+1] = 0
    i+=1

i =0
while i < length:
    if nums[i] == 0:
        del(nums[i])
        counter +=1
        length-=1
        i-=1
    i+=1
j=0
while j<counter:
    nums.append(0)
    j+=1
    
print(nums)