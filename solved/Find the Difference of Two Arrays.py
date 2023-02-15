nums1 = [1,2,3]
nums2 = [2,4,6]
nums1 = [1,2,3,3]
nums2 = [1,1]
res1 =[]
res2 =[]
len_nums1 = len(nums1)
len_nums2 = len(nums2)
if len_nums1 > len_nums2:
    k = len_nums1
else:
    k = len_nums2

i = 0
while i < k:
    if i < len_nums1:
        if nums1[i] not in nums2 and nums1[i] not in res1:
            res1.append(nums1[i])
    if i < len_nums2:
        if nums2[i] not in nums1 and nums2[i] not in res2:
            res2.append(nums2[i])
    i+=1
result = [res1,res2]
print(result)