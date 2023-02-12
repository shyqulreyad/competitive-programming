num = 2932
nums = [int(x) for x in str(num)]
first_digit = min(nums)
nums.remove(first_digit)
second_digit = min(nums)
nums.remove(second_digit)
first_number = first_digit*10+nums[0]
second_number = second_digit*10+nums[1]
res = first_number+second_number
print(res)