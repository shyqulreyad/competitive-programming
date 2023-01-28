import math
nums = [2,2,1,1,1,1,1,2,2,]
nums = [3,2,3]
nums = [2,2]
nums = [0,0,0]
length = len(nums)
nums.sort()
i = 0
counter = 1
result = []
target = math.ceil(length/2)
print(target)
if length == 1 :
    print (nums)
if length == 2:
    if nums[0] == nums[1]:
        print (nums[0])
    else:
        print (nums)
while i < length:
    if i+1 < length:
        if nums[i] ==nums[i+1]:
            counter+=1
            if counter >= target:
                result.append(nums[i])
                print(nums[i])
        else:
            counter = 1
    i+=1
print(result)