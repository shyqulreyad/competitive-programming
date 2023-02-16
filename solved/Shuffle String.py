s = "codeleet"
indices = [4,5,6,7,0,2,1,3]
res = {}
result = ''
i = 0
while i < len(indices):
    res[indices[i]] = s[i]
    i+=1
j=0
while j <len(indices):
    result+=res[j]
    j+=1
print(result)