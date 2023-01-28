nums = [-100,-98,-1,2,3,4]
length = len(nums)
maximum = 0
i=0
while i < length:
    if nums[i] < 0:
        nums[i] = abs(nums[i])
    i+=1
nums.sort()
if length >= 3:
    print(nums[length-1] * nums[length-2] * nums[length-3])
elif length == 2:
    print(nums[length-1]*nums[length-2])
else:
    print(nums[length-1])
