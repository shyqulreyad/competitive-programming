nums = [0,1,0,3,12];

# for i in nums:
#     if i == 0:
#         nums.remove(i)
#         nums.append(i)
# print(nums)

#write a for loop that iterates through the list with index

j = 0
for i in range(len(nums)):
    if nums[i] != 0:
        nums[j] = nums[i]
        j+=1
for i in range(j,len(nums)):
    nums[i] = 0
        
print(nums)