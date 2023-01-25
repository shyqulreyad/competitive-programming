nums =[4,3,2,7,8,2,3,1]
nums = [1,1,2]
nums = [1]
temp = []
result = []
for i in nums:
    if i in temp:
        result.append(i)
    temp.append(i)
print(result)