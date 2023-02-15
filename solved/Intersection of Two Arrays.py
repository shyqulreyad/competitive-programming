nums1 = [1,2,2,1]
nums2 = [2,2]
res =[]
for i in nums1:
    for j in nums2:
        if i==j:
            if i not in res:
                res.append(i)
print(res)