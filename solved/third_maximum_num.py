nums = [1,-2,3]
nums = list(set(nums))
print(nums)
lenth = len(nums)
print(lenth)
if lenth < 3:
    print(max(nums),'hi')
else:
    nums.sort()
    print(nums[lenth-3],'hey')
    