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

# num = 93
# # If given number is greater than 1
# if num > 1:
#     for i in range(2, int(num/2)+1):
#         print(num,'---',i,'---',(num/2)+1)
#         if (num % i) == 0:
#             print(num, "is not a prime number")
#             break
#     else:
#         print(num, "is a prime number")
# else:
#     print(num, "is not a prime number")

# height = [8,6,2,5,4,8,3,7]
# print(sum(height))

# nums = [1,2,3,1]
# nums= [2,7,9,3,1]
# length = len(nums)
# result_even = 0
# result_odd = 0
# i=0
# while i < length:
#     if i%2 == 0:
#         result_even +=nums[i]
#     else:
#         result_odd += nums[i]
#     i+=1
# if result_even > result_odd:
#     print(result_even)
# else:
#     print(result_odd)

# nums = [-1,0]
# target = -1
# # nums = [2,0,1]
# #nested for loop
# for i in range(len(nums)):
#     for j in range(i+1,len(nums)):
#         if nums[i] + nums[j] == target:
#             print(i+1,j+1)


# lis = ['1', '-4', '3', '-6', '7']
# res = [eval(i) for i in lis]
# print("Modified list is: ", res)

# test_list = ['1', '4', '3', '6', '7']
 
# using loop
# for i in range(0, len(test_list)):
#     test_list[i] = int(test_list[i])
 
# # Printing modified list
# print("Modified list is : " + str(test_list))
# nums = [-2,1,-3,4,-1,2,1,-5,4]
# nums = [5,4,-1,7,8]
# length = len(nums)
# res = []
# counter = 0
# i = 0
# while i < length:
#     if i+1 < length:
#         if nums[i] + nums[i+1] > 0 and nums[i] > nums[i+1]:
#             print(nums[i],nums[i+1])
#             counter += nums[i+1] + nums[i]
#             print(counter)
#         else:
#             res.append(counter)
#             counter = 0
#     i+=1
# print(res)
#MAXIMUM SUB ARRAY
# nums = [-2,-1,-3,-4,-1,-2,-1,-5,-4]
# # nums = [5,4,-1,7,8]
# length = len(nums)
# maximum = 0
# counter = 0
# i = 0
# while i < length:
#     counter += nums[i]
#     if counter > maximum :
#         maximum = counter
#     if counter < 0 :
#         counter = 0
#     i+=1
# print(maximum)

#BEST TIME TO SELL STOCK 
prices = [7,6,4,3,1]
length = len(prices)
min_price = max(prices)
max_profit = 0
i =0
while i < length:
    if prices[i] < min_price:
        min_price = prices[i]
    profit = prices[i]- min_price
    if profit > max_profit:
        max_profit = profit
    i+=1
print(max_profit)

