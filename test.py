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
# prices = [7,6,4,3,1]
# length = len(prices)
# min_price = max(prices)
# max_profit = 0
# i =0
# while i < length:
#     if prices[i] < min_price:
#         min_price = prices[i]
#     profit = prices[i]- min_price
#     if profit > max_profit:
#         max_profit = profit
#     i+=1
# print(max_profit)

# nums1 = [1,2]
# nums2 = [3,5,4]
# res = nums1 + nums2
# print(res)

# nums = [1,2,10,5,7]
# # nums = [1,1,1]
# # nums = [2,3,1,2]
# length = len(nums)
# max_num = 0
# i=0
# while i < length:
#     if max_num < nums[i]:
#         print('ok')
#         max_num = nums[i]
#     else:
#         max_num = 0
#         print('noo')
#     i+=1
# Squares of a Sorted Array
# nums = [-4,-1,0,3,10]
# length = len(nums)
# negative = []
# i = 0
# while i < length:
#     if nums[i] < 0:
#         negative.append(nums[i]*nums[i])
#         nums[i] = 0
#     else:
#         nums[i] = nums[i]*nums[i]
#     i+=1
# if len(negative) == 0:
#     print(nums)

# print(nums)
# print(negative)
# for j in negative:
#     print(j)
#     for i in nums:
#         print(i)

# Squares of a Sorted Array


# find peak element 
# nums = [1,2,1,3,5,6,4]
# nums = [1]
# prev_val = nums[0]
# length = len(nums)
# i =1
# while i < length:
#     if i+1 < length:
#         if prev_val < nums[i] and nums[i] > nums[i+1]:
#             print('got it',i)
    
#     i+=1

# apply operation to an array 
# nums = [1,2,2,1,1,0]
# length = len(nums)
# print(length)
# i=0
# while i < length:
#     if i+1 < length:
#         print(nums[i],nums[i+1])
#         if nums[i] == nums[i+1]:
#             nums[i] =nums[i]*2
#             nums[i+1] = 0
#     i+=1
# print(nums) 

#  Remove Duplicates from Sorted Array
# nums = [0,0,1,1,1,1,2,3,3]
# nums = [1,1,1,2,2,3]

# length = len(nums)
# i = 0 
# test = 0
# while i < length:
#     if i+1 < length:
#         if nums[i] == nums[i+1] and test == 1:
#             del(nums[i])
#             print('deleted',nums[i],'---',i)
#             length -=1
#             test = 0
#             i-=1
#         if nums[i] == nums[i+1]:
#             test = 1
#         else:
#             test = 0
#     i+=1
# print(nums,len(nums))

# #Tail RECURSION
# def rec(n):
#     if n > 0:
#         print(n)
#         rec(n-1)
# rec(10)

# #Head RECURSION
# def rectwo(n):
#     if n>0:
#         print('called')
#         rectwo(n-1)
#         print(n)
# rectwo(10)

#TREE RECURSION
#a function calls itself twice after base condition
# def recThree(n):
#     if n>0:
#         print('called first')
#         recThree(n-1)
#         print(n)
#         print('called second')
#         recThree(n-1)
# recThree(3)


#running sum of 1d array
# nums = [1,2,3,4]
# i = 0 
# total = 0
# length = len(nums)
# while i < length:
#     total+=nums[i]
#     nums[i] = total
#     i+=1
# print(nums)

# nums = [4,3,2,7,8,2,3,1]
# nums = [1,1]
# length = len(nums)
# i = 1
# while i <= length:
#     if i not in nums:
#         print(i)
#     i+=1
# nums = [2,3,-2,4]
# nums = [-2,0,-1]
# length = len(nums)
# maximum = 0
# counter = 1
# i = 0
# while i < length:
#     counter *= nums[i]
#     if counter > maximum :
#         maximum = counter
#     if counter < 0 :
#         counter = 0
#     i+=1
# print(maximum)

# nums = [2,2,1,1,1,2,2]
# nums = [3,2,3]
# length = len(nums)
# nums.sort()
# nums.sort()
# i = 0
# counter = 1
# target = length/2
# while i < length:
#     if i+1 < length:
#         if nums[i] ==nums[i+1]:
#             counter+=1
#             if counter > target:
#                 print(nums[i])
#         else:
#             counter = 1
#     else:
#         print(nums[i])
#     i+=1
# ops = ["5","-2","4","C","D","9","+","+"]
# ops = ["1","C"]
# res = []
# for i in ops:
#     if i.isdigit():
#         res.append(int(i))
#     elif i.startswith("-") and i[1:].isdigit():
#         res.append(int(i))
#     else:
#         print(i,'char',res[len(res)-1])
#         if i == "C":
#             del res[len(res)-1]
#         elif i == "D":
#             temp = 2*res[len(res)-1]
#             res.append(temp)
#         elif i == "+":
#             temp = res[len(res)-2] + res[len(res)-1]
#             res.append(temp)
# print(sum(res))


"""
"5" - Add 5 to the record, record is now [5].
"-2" - Add -2 to the record, record is now [5, -2].
"4" - Add 4 to the record, record is now [5, -2, 4].
"C" - Invalidate and remove the previous score, record is now [5, -2].
"D" - Add 2 * -2 = -4 to the record, record is now [5, -2, -4].
"9" - Add 9 to the record, record is now [5, -2, -4, 9].
"+" - Add -4 + 9 = 5 to the record, record is now [5, -2, -4, 9, 5].
"+" - Add 9 + 5 = 14 to the record, record is now [5, -2, -4, 9, 5, 14].
The total sum is 5 + -2 + -4 + 9 + 5 + 14 = 27.
"""
# nums = [4,4,4,9,2,4]
# nums = [29,47,21,41,13,37,25,7]
# nums = [0,1,2,2,4,4,1]
# length = len(nums)
# prev = 0
# counter = 1
# i =0
# while i <length:
#     # print(nums[i])
#     if nums[i] % 2 == 0:
#         prev = nums[i]
#         # print(nums[i])
#         if prev == nums[i]:
#             counter+=1
#         else:
#             counter =1
        
#     else:
#         counter =1
#     i+=1
# print(counter)


# nums = [4,5,6,7,0,1,2]
# target = 0
# if target in nums:
#     print(nums.index(target))
# else:
#     print(-1)


# nums = [1,2,3,1,1,3]
# counter = 0
# for i in range(len(nums)):
#     for j in range(i+1,len(nums)):
#         if nums[i] == nums[j] and i <j:
#             counter+=1            
# print(counter)

# n = 6
# if n%2 ==0:
#     print(n)
# else:
#     print(n*2)

# s = "is2 sentence4 This1 a3"
# x = s.split()
# lenght = len(x)
# res ={}
# for i in x :
#     k = list(i)
#     index =int(len(k)-1)
#     target = int(k[index])
#     del k[index]
#     l = ''.join(k)
#     res[target-1] = l
# result = ''
# for i in range(lenght):
#     if i == 0:
#         result += res[i]
#     else:
#         result +=' '+ res[i]
# print(result)

# s = "leetcode" 
# wordDict = ["leet","code"]
# s = "applepenapple"
# wordDict = ["apple","pen"]
# s = "catsandog"
# wordDict = ["cats","dog","sand","and","cat"]
# s = "aaaaaaa"
# wordDict = ["aaaa","aaa"]
# s.split()
# word =''
# matched = 0
# target = len(s)
# print(target)
# j = 0
# for i in s:
#     # print(i)
#     j+=1
#     word+=i
#     # print(word)
#     if word in wordDict:
#         print(word,'yes',j)
#         matched +=j
#         j=0
#         word =''
#     else:
#         print(word,'no')

# print(matched)
# if target == matched:
#     print('true')
# else:
#     print('false')

# s = "Let's take LeetCode contest"
# s = "God Ding"
# res =''
# x = s.split()
# for idx, i in enumerate(x):
#     if idx == 0:
#         res+=i[::-1]
#     else:
#         res+= ' '+i[::-1]
# print(res)


# prices = [7,1,5,3,6,4]
# prices = [7,6,4,3,1]
# prices = [1,2,3,4,5]
# prices =[3,3,5,0,0,3,1,4]
# prices = [1,2,3,0,2]
# prices =[1,2,4]
# prices = [1,3,2,8,4,9]
# # prices = [1,3,7,5,10,3]
# length = len(prices)
# min_price = max(prices)
# max_profit = 0
# total = 0
# i =0
# while i < length:
#     if prices[i] < min_price:
#         min_price = prices[i]
#     profit = prices[i]- min_price
#     # print(prices[i],'---',min_price)
#     # print(profit)
#     if profit > max_profit and profit > 2:
#         max_profit = profit
#         total +=profit
#         min_price = prices[i]
#         max_profit = 0
#         i+=1
#         # print(max_profit)
#         # min_price = max(prices)
#     i+=1
# print(total)


# s = "abcdefg"
# s = "abcd"
# s = list(s)
# res=''
# k = 2
# for i in range(k//2):
#     s[i],s[k-i-1] = s[k-i-1],s[i]

# print((res.join(s)))

#reverse string ii
# s = "abcdefg"
# k = 2
# res =''
# for i in range(0,len(s),k):
#     res+=s[i:i+k][::-1]
# print(res)

# s = ["h","e","l","l","o"," ","w","o","r","l","d"]
# s = "abcdefg"
# s = list(s)
# lenght = len(s)
# # print(lenght)
# for i in range(lenght//2):
#     # print(i)
#     # print(s[i],s[lenght-i-1])
#     # print(s[lenght-i-1],s[i])
#     s[i],s[lenght-i-1] = s[lenght-i-1],s[i]
# print(s)

# names = ["Mary","John","Emma"]
# heights = [180,165,170]
# res ={}
# result = []
# for i in range(len(names)):
#     res[heights[i]] = names[i]
# print(res)
# # #sort in descending order
# sorted_keys =sorted(res.keys(),reverse=True)
# for i in sorted_keys:
#     result.append(res[i])
# print(result)

# print(res)
# # print(sorted(res.values()))

# num =[1,2,6,3,0,7,1,7,1,9,7,5,6,6,4,4,0,0,6,3]
# k = 516
# s = [str(integer) for integer in num]
# a_string = "".join(s)

# res = int(a_string)

# result = [int(x) for x in str(res+k)]
# print(result) 

# nums = [13,9,2005,83,77]
# res = []
# for i in nums:
#     for n in str(i):
#         print(int(n))
#         res.append(int(n))
# print(res)
# x = 30
# i = 1
# count = 0
# while i <= x:
#     if i > 9:
#         strr = str(i)
#         list_of_number = list(map(int, strr.strip()))
#         if sum(list_of_number)%2 ==0:
#             count+=1
#     elif i%2==0:
#         count+=1
#     i+=1
# print(count)

# n = 521
# res = 0
# j = 0
# for i in str(n):
#     if j%2==0:
#         res +=int(i)
#     else:
#         res -=int(i)
#     j+=1
# print(res)

# nums = [13,9,2005,83,77]
# res = []
# for i in nums:
#     for n in str(i):
#         print(int(n))
#         res.append(int(n))
# print(res)

# num = 38
# res = 0
# for i in str(num):
#     print(int(i)) 
#     res += int(i)
# print(res)  

# def add_digits(n):
#     res = 0
#     for i in str(n):
#         res+=int(i)
#     if res > 9:
#         return add_digits(res)
#     else:
#         return res

# print(add_digits(1654))

# n = 1
# i=0
# prod =0
# while prod <= n:
#     prod = pow(2,i)
#     if prod == n:
#         print('true')
#     i+=1

# nums = [3,4,5,2]
# max_one = max(nums)
# nums.remove(max_one)
# max_two = max(nums)
# print(max_one,max_two)

costs = [1,3,2,4,1]
coins =7
# costs = [10,6,8,7,7,8]
# coins = 5
# costs = [1,6,3,1,2,5]
# coins = 20
res =0
result = 0
# costs.sort()
print(costs)
j=0
for i in costs:
    j+=1
    res+=i
    if res<=coins:
        result=j
    else:
        res-=i
        j-=1
print(result)

    

    