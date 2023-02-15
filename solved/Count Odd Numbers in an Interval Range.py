low = 800445804
high = 979430543
low = 8
high = 10

# 89492370 expected
result =0
res = (high-low+1)
print(res)
if high%2 !=0 and low%2 !=0:
    res+=1
result = res//2
print(result)