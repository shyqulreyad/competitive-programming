nums = [1,3,0,0,2,0,0,4]
nums = [0,0,0,0,0,0,0,2,0,0]
nums =[2,10,2019]
nums = [1,2,3,4]
dif = nums[1] - nums[0]
print(dif)
result = 0
consecutive = 0
for i in nums :
    if i+dif == i+1:
        result +=1
        if consecutive > 0:
            print(consecutive)
            result += consecutive
        consecutive +=1
    else:
        consecutive = 0
print(consecutive)
