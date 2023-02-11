nums = [2,5,1,3,4,7]
n = 3
res =[]
i =0
while i <n:
    res.append(nums[i])
    res.append(nums[n+i])
    i+=1
print(res)