arr = [17,18,8,4,6,1]
# arr =[400]
if len(arr) ==1:
    print(-1)
maximum =0
res=[-1]
result =[]
i= len(arr)-1
while i>0:
    if arr[i] > maximum:
        maximum = arr[i]
        res.append(maximum)
    i-=1
j= len(res)-1
for i in arr:
    if i ==res[j]:
        j-=1
    result.append(res[j])
print(result)