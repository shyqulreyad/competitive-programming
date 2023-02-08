num = 30
i = 1
count = 0
while i <= num:
    if i > 9:
        strr = str(i)
        list_of_number = list(map(int, strr.strip()))
        if sum(list_of_number)%2 ==0:
            count+=1
    elif i%2==0:
        count+=1
    i+=1
print(count)