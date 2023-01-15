n = 14
res='True'
list1=[]
if n ==1:
    # print('true')
if n<=0:
    print('false')   
for i in range(2,n+1):
    if n % i == 0:
        # cheking i prime or not
        for j in range(2, int(i/2)+1):
            if (i % j) == 0:
                break
        else:
            if i != 2:
                if i!=3:
                    if i!=5:  
                        print('false')             
            else:
                print('true')
# print(res)
