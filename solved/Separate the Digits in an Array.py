nums = [13,9,2005,83,77]
res = []
for i in nums:
    for n in str(i):
        print(int(n))
        res.append(int(n))
print(res)