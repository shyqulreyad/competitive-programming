n = 15
result = []
for j in range(1,int(n+1)) :
    if (j%3) ==0 and (j%5) == 0:
        result.append('FizzBuzz')
    elif (j%3) == 0:
        result.append('Fizz')
    elif(j%5) == 0 :
        result.append('Buzz')
    else:
        result.append(str(j))
print(result)