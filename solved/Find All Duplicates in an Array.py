nums =[4,3,2,7,8,2,3,1]
# nums = [1,1,2]
# nums = [1]
nums.sort()
result = []
# print(nums)
length = len(nums)
i = 0
while i < length:
    if i+1 < length:
        if nums[i] == nums[i+1]:
            result.append(nums[i])
    i+=1
print(result)