merged=nums1+nums2
merged.sort()
n=len(merged)
if n%2==0:
    median1 = merged[n//2]
    median2 = merged[n//2 - 1]
    median =(median1 + median2)/2
else:
    median = merged[n//2]
return median    