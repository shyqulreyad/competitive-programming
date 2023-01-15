# digits =[7,2,8,5,0,9,1,2,9,5,4,9,4,7,0,1,1,1,7,4,0,0,6]
# for i in digits:
#     print(i)
#     for j in digits:
#         print(j,'test')
# nums = [7,2,8,5,0,9,1,2,9,5,4,9,4,7,1,1,1,7,4,6]
# print(nums)
# lenth = len(nums)
# print(lenth)
# i=0
# while i <lenth:
#     if nums[i] == 0:
#         print('deleted')
#         print(lenth)
#         del(nums[i])
#     i+=1
# print(nums)
# def bin(n):
#     if n > 1:
#         bin(n//2)
#     print(n % 2, end="")
# bin(1534236469)
# print()
# bin(4)
# i = True
# while i == True:
#     print('hi there')
#     i = False
# a = [1,2,1]
# for idx, i in enumerate(a):
#     print(i,'--',idx)
#     if i % 2 == 0:
#         print('even',i)
#         if i +1 == 0
#     else:
#         print('odd',i)
# n = 5
# if n > 1:
# 	for i in range(2, int(n/2)+1):
# 		if (n % i) == 0:
# 			print(num, "is not a prime number")
# 		break
# 	else:
# 		print(n, "is a prime number")
# # If the number is less than 1, its also not a prime number.
# else:
# 	print(n, "is not a prime number")

num = 93
# If given number is greater than 1
if num > 1:
    for i in range(2, int(num/2)+1):
        print(num,'---',i,'---',(num/2)+1)
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")
