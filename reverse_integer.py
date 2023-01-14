x = 1463847412
#check if x is larger than 32 bit

change = False
if x < 0:
    x= abs(x)
    change = True
stt = str(x)
res = stt[::-1]
res_2 = int(res)
if (x<=(2**31)-1) and (x>=(-2**31)):
    if (res_2<=(2**31)-1) and (res_2>=(-2**31)):
        if change :
            res = '-'+res
            result = int(res)
        result = int(res)
else:
    result = 0
print(result)