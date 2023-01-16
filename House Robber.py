nums = [1,2,3,1]
nums= [2,7,9,3,1]
nums = [2,1,1,2]
length = len(nums)
result_even = 0
result_odd = 0
i=0
while i < length:
    if i%2 == 0:
        result_even +=nums[i]
    else:
        result_odd += nums[i]
    i+=1
if result_even > result_odd:
    print(result_even)
else:
    print(result_odd)