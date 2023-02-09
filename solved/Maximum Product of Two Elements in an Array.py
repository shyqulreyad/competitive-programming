nums = [3,4,5,2]
max_one = max(nums)
nums.remove(max_one)
max_two = max(nums)
print((max_one - 1)* (max_two-1))
