nums = [1,2,3,4,5]
target = 4
lenght = len(nums)
i = 0
j = lenght -1
while i <= j:
    if nums[i] == target:
        print(nums[i])
    if nums[j] == target:
        print(nums[j])
    i+=1
    j-=1
print('-1')