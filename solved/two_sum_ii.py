# numbers = [-1,0]
# target = -1
numbers = [2,7,11,15]
target = 9

remainder = []
for i in range(len(numbers)):
    remain = target-numbers[i]
    if (numbers[i] in remainder):
        print(remainder.index(numbers[i])+1,i+1)
    else:
        remainder.insert(i,remain)

