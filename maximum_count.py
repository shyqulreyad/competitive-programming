nums = [-2,-1,-1,1,2,3]
positive = 0
negative = 0
for i in nums:
    if i > 0:
        positive+=1
    if i < 0:
        negative +=1
if positive > negative:
    print(positive)
else:
    print(negative)