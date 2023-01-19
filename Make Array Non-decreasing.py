nums = [5,3,4,4,7,3,6,11,8,5,11]
min_num= max(nums)
max_num = min(nums)
length = len(nums)
i =0
while i < length:
    if nums[i] < min_num:
        print(nums[i],'min val')
    i+=1