x = 12300
#check if x is larger than 32 bit
change = False
if x < 0:
    x= abs(x)
    change = True
stt = str(x)
res = stt[::-1]
if change :
    res = '-'+res
    result = int(res)
    print(result)
result = int(res)
print(result)