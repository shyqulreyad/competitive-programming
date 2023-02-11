accounts = [[2,8,7],[7,1,3],[1,9,5]]
res = 0
for i in accounts:
    if sum(i) > res:
        res = sum(i)
print(res)