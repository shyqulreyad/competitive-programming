arr = [17,18,5,4,6,1]
arr =[400]
maximum =-1
for i in range(len(arr) - 1, -1, -1):
    if arr[i] > maximum:
        new_maximum = arr[i]
    arr[i] = maximum
    maximum = new_maximum
print(arr)

# Solution with while loop
maximum =-1
i = len(arr)-1
while i >=0:
    if arr[i] > maximum:
        new_maximum = arr[i]
    arr[i] = maximum
    maximum = new_maximum
    i-=1
print(arr)
