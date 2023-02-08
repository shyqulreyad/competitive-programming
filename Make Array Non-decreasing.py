nums = [5,3,4,4,7,3,6,11,8,5,11]
# length = len(nums)
# prev = nums[0]
# counter = 0
# i =1
# while i < length:
#     if prev > nums[i]:
#         print(nums[i])
#         nums.remove(nums[i])
#         length-=1
#     prev = nums[i]
#     i+=1
# counter+=1
# print(counter)
# print(nums)
nums = [4,5,7,7,13]
nums = [10,1,2,3,4,5,6,1,2,3]
# nums =[5,11,7,8,11]   #expected output = 2
nums =[10,6,5,10,15]    #expected output = 1
# nums = [5,3,4,4,7,3,6,11,8,5,11]
counter = 0

def non_decreasing(nums,counter):
    length = len(nums)
    prev = nums[0]
    rec_counter = 0
    i =0
    while i < length:
        if i <length and prev > nums[i] or nums[i] > nums[i+1]:
            prev = nums[i]
            nums.remove(nums[i])
            rec_counter+=1
            length-=1
            # i-=1
        else:
            prev = nums[i] 
        i+=1
    # print(rec_counter)
    if rec_counter > 0:
        counter+=1
        print(counter)
        return non_decreasing(nums,counter)
    return counter

print(non_decreasing(nums,counter))