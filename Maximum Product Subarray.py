# nums = [2,3,-2,4]
# nums = [-2,0,-1]
# nums = [-3,-1,-1]
# nums = [-2,3,-4]
# nums = [0,2]
nums = [2,-5,-2,-4,3]
print(nums)
length = len(nums)
maximum = -999999
counter = 0
i = 0
while i < length:
    counter += nums[i]
    if counter > maximum :
        maximum = counter
    if counter < 0 :
        counter = 0
    i+=1
print(maximum)













# if nums[0] > 0:
#     counter = nums[0]
# else:
#     counter = 1
# i = 1
# if length == 1:
#     maximum = nums[0]
#     print (maximum)
# while i < length:
#     counter *= nums[i]
#     if counter > maximum :
#         maximum = counter
#     if counter < 0 :
#         counter = 1
#     i+=1
# print (maximum)