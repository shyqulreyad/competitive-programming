nums = [4,3,2,7,8,2,3,1]
nums = [2,2]
result = []
length = len(nums)
i = 1
while i <= length:
    if i not in nums:
        result.append(i)
    i+=1
print(result)