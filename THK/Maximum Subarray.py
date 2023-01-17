nums = [-2,-1,-3,-4,-1,-2,-1,-5,-4]
length = len(nums)
maximum = 0
counter = 0
i = 0
while i < length:
    counter += nums[i]
    if counter > maximum :
        maximum = counter
    if counter < 0 :
        counter = 0
    i+=1
print(maximum)

