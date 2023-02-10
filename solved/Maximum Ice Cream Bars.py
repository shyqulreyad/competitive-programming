costs = [1,3,2,4,1]
coins =7
costs = [10,6,8,7,7,8]
coins = 5
costs = [1,6,3,1,2,5]
coins = 20
res =0
result = 0
costs.sort()
print(costs)
j=0
for i in costs:
    j+=1
    res+=i
    if res<=coins:
        result=j
print(result)