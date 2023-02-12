nums = [1,15,6,3]
num =0
for i in nums:
    if i <10:
        num +=i
    else:
        for j in str(i):
            num+=int(j)
res = sum(nums) - num
print(res)