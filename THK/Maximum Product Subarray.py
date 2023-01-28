nums = [2,3,-2,4]
nums = [-2,0,-1]
length = len(nums)
maximum = 0
counter = 1
i = 0
while i < length:
    counter *= nums[i]
    if counter > maximum :
        maximum = counter
    if counter < 0 :
        counter = 0
    i+=1
print(maximum)