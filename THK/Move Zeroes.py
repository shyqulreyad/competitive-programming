nums = [2,0,2,1,1,0]
nums = [0,1,0,3,12]
nums = [0,0,1]
length = len(nums)
# counter = 1
# nums = [0]
i =0
while i < length:
    if nums[i] == 0:
        del(nums[i])
        length-=1
    i+=1
print(nums)
    
# for i in range(length):
#     if i == 0:
#         print(i)
#         print('index will be',length - counter)
#         counter +=1
#     else:
#         print(i)
# print(nums)