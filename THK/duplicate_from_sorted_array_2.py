nums = [0,0,1,1,1,1,2,3,3]
nums = [1,1,1,2,2,3]

length = len(nums)
i = 0 
test = 0
while i < length:
    if i+1 < length:
        if nums[i] == nums[i+1] and test == 1:
            del(nums[i])
            print('deleted',nums[i],'---',i)
            length -=1
            test = 0
            i-=1
        if nums[i] == nums[i+1]:
            test = 1
        else:
            test = 0
    i+=1
print(nums,len(nums))