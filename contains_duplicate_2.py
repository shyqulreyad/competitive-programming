# nums = [1,2,3,1]
# k = 3
# nums = [1,2,3,1,2,3]
# k = 2
nums =[1,0,1,1]
k = 1
test= []
for i in range(len(nums)):
    if nums[i] in test:
        test.insert(i,nums[i])
        print('duplicate',test.index(nums[i]),'---',i)
        test_index = test.index(nums[i])
        print(test_index)
        if (i - test_index) <= k:
            print('true')
        # print(test.index(nums[i]))
        test[test_index] = None
    else:
        test.insert(i,nums[i])
print('false')
print(test)
# Time Limit Exceeded