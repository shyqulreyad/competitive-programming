nums = [1,2,3,1]
test= []
for i in range(len(nums)):
    if (nums[i] not in test):
        test.append(nums[i])
    else:
        print('ture')
print('false')