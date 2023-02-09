n = 521
res = 0
j = 0
for i in str(n):
    if j%2==0:
        res +=int(i)
    else:
        res -=int(i)
    j+=1
print(res)