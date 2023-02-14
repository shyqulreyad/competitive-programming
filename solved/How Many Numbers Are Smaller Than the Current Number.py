nums = [8,1,2,2,3]
res = []
counter = 0
for i in nums:
    for j in nums:
        if i > j:
            counter+=1
    res.append(counter)
    counter=0
print(res)