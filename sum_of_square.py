c = 3
i = 0
test = []
counter = 0
while i < c :
    if (i*i < c):
        t = c - i*i
        test.append(t)
        if(t in test):
            counter +=1
        print(test)
    i+=1
if counter < 2:
    print('false') 
else:
    print('ture')

print(test)
print(counter)