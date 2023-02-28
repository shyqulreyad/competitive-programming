encoded = [1,2,3]
first = 1
encoded = [6,2,7,3]
first = 4
arr = [first]
i = 0
while i < len(encoded):
    print(encoded[i])
    j = encoded[i] ^ arr[i]
    arr.append(j)
    i+=1

print(arr)