s = "is2 sentence4 This1 a3"
x = s.split()
lenght = len(x)
res ={}
for i in x :
    k = list(i)
    index =int(len(k)-1)
    target = int(k[index])
    del k[index]
    l = ''.join(k)
    res[target-1] = l
result = ''
for i in range(lenght):
    if i == 0:
        result += res[i]
    else:
        result +=' '+ res[i]
print(result)