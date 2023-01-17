nums = [5]
target = 5
lenght = len(nums)
i = 0
j = lenght -1
while i <= j:
    print(nums[i],'ii')
    if nums[i] == target:
        print(nums[i])
    if nums[j] == target:
        print(nums[j])
    print(nums[j],'jj')
    i+=1
    j-=1
print('-1')