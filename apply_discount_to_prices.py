sentence= "there are $100 $2 and 5$ candies in the shop"
discount = 20
result = ""
x = sentence.split()
for i in x :
    if(list(i)[0] == '$'):
        digit =list(i[1])
        num1 = ''.join([str(elem) for elem in digit])
        convertedNum1 = int(num1)
        res = (discount/ 100)*convertedNum1
        print(res)
        price = str(res)
        result += list(i)[0]+ price + ' ' 
    else:
        result += i + ' '
print( result)
        
