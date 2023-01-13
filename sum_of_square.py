c = 4
i = 0
test = []
counter = 0
while i < c :
    if (i*i < c):
        t = c - i*i
        if(t in test):
            counter+=1
        test.append(t)
    i+=1
if counter < 2:
    print('false') 
else:
    print('ture')

print(test)