num = 9669
res=''
notchanged = True
for i in str(num):
    if notchanged:
        if i =='6':
            res+='9'
            notchanged = False
        else:
            res+=i
    else:
        res+=i
print(res)