n = 234
sum = 0
product = 1
for i in str(n):
    sum += int(i)
    product *= int(i)
print(product - sum)
