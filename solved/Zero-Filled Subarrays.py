# nums = [1,3,0,0,2,0,0,4]
nums = [0,0,0,0,0,0,0,2,0,0]
# nums =[2,10,2019]
result = 0
consecutive = 0
for i in nums :
    if i == 0:
        result +=1
        if consecutive > 0:
            print(consecutive)
            result += consecutive
        consecutive +=1
    else:
        consecutive = 0
print(result)