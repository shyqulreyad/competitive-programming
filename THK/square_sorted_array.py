nums = [-4,-1,0,3,10]
length = len(nums)
i = 0
prev = 0
while i < length:
    if prev < nums[i] * nums[i]:
        print('chng')
    prev =nums[i] = nums[i]*nums[i]
    print(prev)
    i+=1
print(nums)
# # nums.sort()
# # print(nums)

# nums = [-4,-1,0,3,10]
# length = len(nums)
# negative = []
# i = 0
# while i < length:
#     if nums[i] < 0:
#         negative.append(nums[i]*nums[i])
#         nums[i] = 0
#     else:
#         nums[i] = nums[i]*nums[i]
#     i+=1
# if len(negative) == 0:
#     return nums


# for j in negative:
#     k = length-1
#     while k >= 0:
#         if j > nums[k]:
#             temp = j
#             j = nums[k]
#             nums[k] = temp
#         k-=1

# print(nums)