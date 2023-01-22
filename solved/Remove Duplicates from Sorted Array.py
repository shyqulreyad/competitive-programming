nums = [0,0,1,1,1,2,2,3,3,4]
# nums = [1,1,2]

length = len(nums)
i = 0 
while i < length:
    if i+1 < length:
        if nums[i] == nums[i+1]:
            del(nums[i])
            length -=1
            i-=1
    i+=1
print(len(nums))