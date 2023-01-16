nums = [2,0,2,1,1,0]
# nums = [2,0,1]
#nested for loop
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i] > nums[j]:
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
print(nums)
# while i < length:
#     if i+1 <length:
#         if nums[i] > nums[i+1]:
#             print(nums[i],'---',nums[i+1],i)
#             temp = nums[i]
#             nums[i] = nums[i+1]
#             nums[i+1] = temp
#     i+=1

# print(nums)