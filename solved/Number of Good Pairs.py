nums = [1,2,3,1,1,3]
counter = 0
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i] == nums[j] and i <j:
            counter+=1            
print(counter)