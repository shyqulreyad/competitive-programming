candies = [2,3,5,1,3]
extraCandies = 3
candies = [4,2,1,1,2]
extraCandies = 1
res = []
max_value = max(candies)
for i in candies:
    if i+extraCandies >= max_value:
        res.append(True)
    else:
        res.append(False)
print(res)