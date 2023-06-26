c = 5
i = 1
test = []
counter = 0
while i < c :
    if (i*i < c):
        t = c - i*i
        print(t)
        if(t in test):
            counter +=1
            print('ture')
        print(test)
        test.append(t)
    i+=1
if counter < 2:
    print('false') 
else:
    print('ture')

print(test)
# print(counter)