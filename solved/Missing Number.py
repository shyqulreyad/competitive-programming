# nums = [9,6,4,2,3,5,7,0,1]
# nums = [0,1]
nums = [3,0,1,2,4,6,7,8,9,10]
nums.sort()
length = len(nums)
result = 0
i =0
while i <length :
    if i == nums[i]:
        result +=1
    i+=1
print(result)