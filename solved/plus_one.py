digits = [9,9,9,9,9,9,9]
num1 = ''.join([str(elem) for elem in digits])
convertedNum1 = int(num1)
res = convertedNum1 + 1
result = [int(x) for x in str(res)]
print(result)