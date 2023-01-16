numbers = [2,3,4]
target = 6
remainder = []
for i in range(len(numbers)):
    num = target - numbers[i]
    if num in remainder:
        print('hi')
    else:
        remainder.append(i=>numbers[i])
print(remainder)