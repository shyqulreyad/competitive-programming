sentence= "there are $1 $2 and 5$ candies in the shop"
discount =50
result = ""
x = sentence.split()
lenth = len(x)
j = 0
for i in x :
    j+=1
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
            price = price = f'{final_res:.2f}'
            if j == 1:
                result += '$'+ price
            else:
                result += ' '+'$'+ price
        else:
            if j == 1:
                result += '$'+ num
            else:
                result +=' '+ '$'+ num
    else:
        if j == 1:
            result += i
        else:
            result += ' '+ i

print(result)
        
