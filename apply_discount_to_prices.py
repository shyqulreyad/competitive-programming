sentence= "there are $1 $2 and 5$ candies in the shop"
discount =50
result = ""
x = sentence.split()
for i in x :
    if(list(i)[0] == '$'):
        digit =list(i)
        lenth = len(digit)
        num = ''
        i = 1
        while i < lenth:
            num +=digit[i]
            i+=1
        num.isdigit()
        if num.isdigit():
            convertedNum1 = int(num)
            res = convertedNum1*(discount/100)
            final_res = convertedNum1 - res
            price = str(final_res)
            print(price)
            result += '$'+ price + ' ' 
        else:
            result += '$'+ num + ' '
    else:
        result += i + ' '
print(result)
        
