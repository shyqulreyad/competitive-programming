n = 10
# If given number is greater than 1
# counter = 0
# j = 0
# if n > 1:
#     while j <= n:
#         for i in range(2, int(j/2)+1):
#             if (j % i) == 0:
#                 print(j, "is not a prime number")
#                 break
#             else:
#                 print(j, "is a prime number")
#                 counter += 1
#     j+=1
# else:
#     print('zero')

# print(counter)

n =100
primes = [2]
if n > 1:
    counter =1
    j=0
    while j <=n:
        if j < 1 :
            for i in range(2,int(j/2)+1):
                print(j,'---',i)
                if (j % i) == 0:
                    print(j,'not prime')
                    break
                else:
                    print(j,'prime')
                    #add to primes if doesnt exist
                    if j not in primes:
                        primes.append(j)
        j+=1
else:
    print('zero')
lenth = len(primes)
print(primes)
print(lenth)