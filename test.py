digits =[7,2,8,5,0,9,1,2,9,5,4,9,4,7,0,1,1,1,7,4,0,0,6]
for i in digits:
    print(i)
    for j in digits:
        print(j,'test')
nums = [7,2,8,5,0,9,1,2,9,5,4,9,4,7,1,1,1,7,4,6]
print(nums)
lenth = len(nums)
print(lenth)
i=0
while i <lenth:
    if nums[i] == 0:
        print('deleted')
        print(lenth)
        del(nums[i])
    i+=1
print(nums)
def bin(n):
    if n > 1:
        bin(n//2)
    print(n % 2, end="")
bin(1534236469)
print()
bin(4)
i = True
while i == True:
    print('hi there')
    i = False
a = [1,2,1]
for idx, i in enumerate(a):
    print(i,'--',idx)
    if i % 2 == 0:
        print('even',i)
        # if i +1 == 0
    else:
        print('odd',i)
n = 5
if n > 1:
	for i in range(2, int(n/2)+1):
		if (n % i) == 0:
			print(n, "is not a prime number")
		break
	else:
		print(n, "is a prime number")
# If the number is less than 1, its also not a prime number.
else:
	print(n, "is not a prime number")

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

height = [8,6,2,5,4,8,3,7]
print(sum(height))

nums = [1,2,3,1]
nums= [2,7,9,3,1]
length = len(nums)
result_even = 0
result_odd = 0
i=0
while i < length:
    if i%2 == 0:
        result_even +=nums[i]
    else:
        result_odd += nums[i]
    i+=1
if result_even > result_odd:
    print(result_even)
else:
    print(result_odd)

nums = [-1,0]
target = -1
nums = [2,0,1]
#nested for loop
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i] + nums[j] == target:
            print(i+1,j+1)


lis = ['1', '-4', '3', '-6', '7']
res = [eval(i) for i in lis]
print("Modified list is: ", res)

test_list = ['1', '4', '3', '6', '7']
 
# using loop
for i in range(0, len(test_list)):
    test_list[i] = int(test_list[i])
 
# Printing modified list
print("Modified list is : " + str(test_list))
nums = [-2,1,-3,4,-1,2,1,-5,4]
nums = [5,4,-1,7,8]
length = len(nums)
res = []
counter = 0
i = 0
while i < length:
    if i+1 < length:
        if nums[i] + nums[i+1] > 0 and nums[i] > nums[i+1]:
            print(nums[i],nums[i+1])
            counter += nums[i+1] + nums[i]
            print(counter)
        else:
            res.append(counter)
            counter = 0
    i+=1
print(res)
# MAXIMUM SUB ARRAY
nums = [-2,-1,-3,-4,-1,-2,-1,-5,-4]
# nums = [5,4,-1,7,8]
length = len(nums)
maximum = 0
counter = 0
i = 0
while i < length:
    counter += nums[i]
    if counter > maximum :
        maximum = counter
    if counter < 0 :
        counter = 0
    i+=1
print(maximum)

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
nums = [1,2,3,4]
i = 0 
total = 0
length = len(nums)
while i < length:
    total+=nums[i]
    nums[i] = total
    i+=1
print(nums)

nums = [4,3,2,7,8,2,3,1]
nums = [1,1]
length = len(nums)
i = 1
while i <= length:
    if i not in nums:
        print(i)
    i+=1
nums = [2,3,-2,4]
nums = [-2,0,-1]
length = len(nums)
maximum = 0
counter = 1
i = 0
while i < length:
    counter *= nums[i]
    if counter > maximum :
        maximum = counter
    if counter < 0 :
        counter = 0
    i+=1
print(maximum)

nums = [2,2,1,1,1,2,2]
nums = [3,2,3]
length = len(nums)
nums.sort()
nums.sort()
i = 0
counter = 1
target = length/2
while i < length:
    if i+1 < length:
        if nums[i] ==nums[i+1]:
            counter+=1
            if counter > target:
                print(nums[i])
        else:
            counter = 1
    else:
        print(nums[i])
    i+=1
ops = ["5","-2","4","C","D","9","+","+"]
ops = ["1","C"]
res = []
for i in ops:
    if i.isdigit():
        res.append(int(i))
    elif i.startswith("-") and i[1:].isdigit():
        res.append(int(i))
    else:
        print(i,'char',res[len(res)-1])
        if i == "C":
            del res[len(res)-1]
        elif i == "D":
            temp = 2*res[len(res)-1]
            res.append(temp)
        elif i == "+":
            temp = res[len(res)-2] + res[len(res)-1]
            res.append(temp)
print(sum(res))


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
nums = [4,4,4,9,2,4]
nums = [29,47,21,41,13,37,25,7]
nums = [0,1,2,2,4,4,1]
length = len(nums)
prev = 0
counter = 1
i =0
while i <length:
    # print(nums[i])
    if nums[i] % 2 == 0:
        prev = nums[i]
        # print(nums[i])
        if prev == nums[i]:
            counter+=1
        else:
            counter =1
        
    else:
        counter =1
    i+=1
print(counter)


nums = [4,5,6,7,0,1,2]
target = 0
if target in nums:
    print(nums.index(target))
else:
    print(-1)


nums = [1,2,3,1,1,3]
counter = 0
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i] == nums[j] and i <j:
            counter+=1            
print(counter)

n = 6
if n%2 ==0:
    print(n)
else:
    print(n*2)

s = "is2 sentence4 This1 a3"
x = s.split()
lenght = len(x)
res ={}
for i in x :
    k = list(i)
    index =int(len(k)-1)
    target = int(k[index])
    del k[index]
    l = ''.join(k)
    res[target-1] = l
result = ''
for i in range(lenght):
    if i == 0:
        result += res[i]
    else:
        result +=' '+ res[i]
print(result)

s = "leetcode" 
wordDict = ["leet","code"]
s = "applepenapple"
wordDict = ["apple","pen"]
s = "catsandog"
wordDict = ["cats","dog","sand","and","cat"]
s = "aaaaaaa"
wordDict = ["aaaa","aaa"]
s.split()
word =''
matched = 0
target = len(s)
print(target)
j = 0
for i in s:
    # print(i)
    j+=1
    word+=i
    # print(word)
    if word in wordDict:
        print(word,'yes',j)
        matched +=j
        j=0
        word =''
    else:
        print(word,'no')

print(matched)
if target == matched:
    print('true')
else:
    print('false')

s = "Let's take LeetCode contest"
s = "God Ding"
res =''
x = s.split()
for idx, i in enumerate(x):
    if idx == 0:
        res+=i[::-1]
    else:
        res+= ' '+i[::-1]
print(res)


prices = [7,1,5,3,6,4]
prices = [7,6,4,3,1]
prices = [1,2,3,4,5]
prices =[3,3,5,0,0,3,1,4]
prices = [1,2,3,0,2]
prices =[1,2,4]
prices = [1,3,2,8,4,9]
# prices = [1,3,7,5,10,3]
length = len(prices)
min_price = max(prices)
max_profit = 0
total = 0
i =0
while i < length:
    if prices[i] < min_price:
        min_price = prices[i]
    profit = prices[i]- min_price
    # print(prices[i],'---',min_price)
    # print(profit)
    if profit > max_profit and profit > 2:
        max_profit = profit
        total +=profit
        min_price = prices[i]
        max_profit = 0
        i+=1
        # print(max_profit)
        # min_price = max(prices)
    i+=1
print(total)


s = "abcdefg"
s = "abcd"
s = list(s)
res=''
k = 2
for i in range(k//2):
    s[i],s[k-i-1] = s[k-i-1],s[i]

print((res.join(s)))

# reverse string ii
s = "abcdefg"
k = 2
res =''
for i in range(0,len(s),k):
    res+=s[i:i+k][::-1]
print(res)

s = ["h","e","l","l","o"," ","w","o","r","l","d"]
s = "abcdefg"
s = list(s)
lenght = len(s)
# print(lenght)
for i in range(lenght//2):
    # print(i)
    # print(s[i],s[lenght-i-1])
    # print(s[lenght-i-1],s[i])
    s[i],s[lenght-i-1] = s[lenght-i-1],s[i]
print(s)

names = ["Mary","John","Emma"]
heights = [180,165,170]
res ={}
result = []
for i in range(len(names)):
    res[heights[i]] = names[i]
print(res)
# #sort in descending order
sorted_keys =sorted(res.keys(),reverse=True)
for i in sorted_keys:
    result.append(res[i])
print(result)

print(res)
# print(sorted(res.values()))

num =[1,2,6,3,0,7,1,7,1,9,7,5,6,6,4,4,0,0,6,3]
k = 516
s = [str(integer) for integer in num]
a_string = "".join(s)

res = int(a_string)

result = [int(x) for x in str(res+k)]
print(result) 

nums = [13,9,2005,83,77]
res = []
for i in nums:
    for n in str(i):
        print(int(n))
        res.append(int(n))
print(res)
x = 30
i = 1
count = 0
while i <= x:
    if i > 9:
        strr = str(i)
        list_of_number = list(map(int, strr.strip()))
        if sum(list_of_number)%2 ==0:
            count+=1
    elif i%2==0:
        count+=1
    i+=1
print(count)

n = 521
res = 0
j = 0
for i in str(n):
    if j%2==0:
        res +=int(i)
    else:
        res -=int(i)
    j+=1
print(res)

nums = [13,9,2005,83,77]
res = []
for i in nums:
    for n in str(i):
        print(int(n))
        res.append(int(n))
print(res)

num = 38
res = 0
for i in str(num):
    print(int(i)) 
    res += int(i)
print(res)  

def add_digits(n):
    res = 0
    for i in str(n):
        res+=int(i)
    if res > 9:
        return add_digits(res)
    else:
        return res

print(add_digits(1654))

n = 1
i=0
prod =0
while prod <= n:
    prod = pow(2,i)
    if prod == n:
        print('true')
    i+=1

nums = [3,4,5,2]
max_one = max(nums)
nums.remove(max_one)
max_two = max(nums)
print(max_one,max_two)

costs = [1,3,2,4,1]
coins =7
costs = [10,6,8,7,7,8]
coins = 5
costs = [1,6,3,1,2,5]
coins = 20
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

address = "1.1.1.1"
print(address.replace('.','[.]'))
operations = ["--X","X++","X++"]
x = 0
for i in operations:
    if i == '++X' or i == 'X++':
        x+=1
    else:
        x-=1
print(x)
accounts = [[2,8,7],[7,1,3],[1,9,5]]
res = 0
for i in accounts:
    if sum(i) > res:
        res = sum(i)
print(res)

nums = [2,5,1,3,4,7]
res =[]
n = 3
i =0
while i <n:
    res.append(nums[i])
    res.append(nums[n+i])
    i+=1
print(res)

grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
counter =0
cache ={}
j = 0
for i in grid:
    cache[j] =i
    j+=1
# print(cache)
k =0
while k <j:
    print(cache[k])
    k+=1
jewels = "aA"
stones = "aAAbbbb"
res = 0
for i in stones:
    if i in jewels:
        res +=1
print(res)


num = 2932
nums = [int(x) for x in str(num)]
first_digit = min(nums)
nums.remove(first_digit)
second_digit = min(nums)
nums.remove(second_digit)
first_number = first_digit*10+nums[0]
second_number = second_digit*10+nums[1]
res = first_number+second_number
print(res)
nums = [1,15,6,3]
num =0
for i in nums:
    if i <10:
        num +=i
    else:
        for j in str(i):
            num+=int(j)
res = sum(nums) - num
print(res)

nums = [5,2,6,1]
temp =nums[0]
res =[]
def countNums(temp):
    count = 0
    for i in nums:
        if i<temp:
            count+=1
    res.append(count)
    nums.remove(nums[0])
    if len(nums) >0:
        return countNums(nums[0])
    return res

print(countNums(temp))

nums = [5,2,6,1]
i = 0
while i < len(nums):
    print(nums[i])
    i+=1

sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
count = 0
for i in sentences:
    j =i.split(' ')
    count = len(j)
    if len(j) > count:
        count = len(j)
print(count)

s = "codeleet"
indices = [4,5,6,7,0,2,1,3]
res = {}
result = ''
i = 0
while i < len(indices):
    res[indices[i]] = s[i]
    i+=1
j=0
while j <len(indices):
    result+=res[j]
    j+=1
print(result)

nums = [8,1,2,2,3]
res = []
counter = 0
for i in nums:
    for j in nums:
        if i > j:
            counter+=1
    res.append(counter)
    counter=0
print(res)



for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i] > nums[j]:
            counter +=1
    res.append(counter)
    counter =0
print(res)
    

num = 9669
res=''
notchanged = True
for i in str(num):
    if notchanged:
        if i =='6':
            res+='9'
            notchanged = False
        else:
            res+=i
    else:
        res+=i
print(res)

candies = [2,3,5,1,3]
extraCandies = 3
candies = [4,2,1,1,2]
extraCandies = 1
res = []
max_value = max(candies)
for i in candies:
    if i+extraCandies >= max_value:
        res.append(True)
    else:
        res.append(False)
print(res)

low = 800445804
high = 979430543
count = 0
while low <=high:
    if low%2 != 0:
        count+=1
        low+=1
    low+=1
print(count)

nums1 = [1,2,2,1]
nums2 = [2,2]
res =[]
for i in nums1:
    for j in nums2:
        if i==j:
            if i not in res:
                res.append(i)
print(res)

nums1 = [1,2,3]
nums2 = [2,4,6]
nums1 = [1,2,3,3]
nums2 = [1,1]
res1 =[]
res2 =[]
len_nums1 = len(nums1)
len_nums2 = len(nums2)
if len_nums1 > len_nums2:
    k = len_nums1
else:
    k = len_nums2

i = 0
while i < k:
    if i < len_nums1:
        if nums1[i] not in nums2 and nums1[i] not in res1:
            res1.append(nums1[i])
    if i < len_nums2:
        if nums2[i] not in nums1 and nums2[i] not in res2:
            res2.append(nums2[i])
    i+=1
result = [res1,res2]
print(result)

low = 800445804
high = 979430543
low = 8
high = 10

# 89492370 expected
result =0
res = (high-low+1)
print(res)
if high%2 !=0 and low%2 !=0:
    res+=1
result = res//2
print(result)

nums =[1,2,3,4,5,6,7]
nums= [1,3,5]
res = []
for i in range(len(nums)):
    # res.append(nums[i])
    for j in range(i+1,len(nums)):
        res.append(nums[i])
        # res.append(nums[j])
    print(res)

nums = [3,4,-1,1]
nums = [1]
print(len(nums))
i=1
while i < len(nums):
    if i not in nums:
        print(i)
    i+=1
print(i)

height = [4,2,0,3,2,5]
height = [0,1,0,2,1,0,1,3,2,1,2,1]
biggest =0
traped = 0
for i in height:
    print(i)





for i in height:
    if i < top:
        print(i,'---',traped)
        traped += top-i
    else:
        top=i
print(traped)


arr = [1,2,3,4,5]
k = 2
# arr.sort()
print(arr)
m = ((len(arr)-1 )//2)
print(m)
i = 0
j = len(arr)
while i < j:
    
    if arr[i]-arr[m] >= arr[j]-arr[m]:
        print(arr[i])
    i+=1

s = "4193 with words"
s = "  words 97"
s ="-91283472332"
s ="3.14159"
res=''
for i in s:
    if i.isalpha():
        print(i)
        if len(res)==0:
            print(0)
    if len(res) !=0:
        if i == '.':
            break
    if i.isnumeric():
        res+=i
    elif i == '-':
        res+='-'

if (int(res)>(2**31)-1) or (int(res)<(-2**31)):
    x = max(-2**31, min(int(res), 2**31 - 1))
    print(x)
print(res)

num = 28
# num =99999991
sumation = 0
i = 1
while i<=num/2:
    if num%i==0:
        sumation+=i
        print(i)
    i+=1

if sumation == num:
    print('True')
else:
    print('False')

s = "abcabcbb"
s = "pwwkew"
s = ""
s ="aab"
s ="dvdf"
temp =[]
counter = 0
maximum = []
temp = list(s)
 
i =0
while i< len(temp):
    temp.remove(temp[i])
    print(s)
    print(temp)
    if s[i] not in temp:
        maximum.append(s[i])
    i+=1
    print(maximum)










i =0
while i < len(s):
    if s[i] not in temp:
        temp.append(s[i])
        counter+=1
    else:
        maximum.append(counter)
        counter=0
        temp =[]
        i-=1
    maximum.append(counter)
    i+=1
maximum.append(counter)
print(maximum)



for i in s:
    print(i)
    if i not in temp:
        temp.append(i)
        counter+=1
        print(counter)
    else:
        maximum.append(counter)
        counter =1
        temp=[]
    maximum.append(counter)
maximum.append(counter)

print(maximum)


# arr =[400]
if len(arr) ==1:
    print(-1)
maximum =0
res=[-1]
result =[]
i= len(arr)-1
while i>0:
    if arr[i] > maximum:
        maximum = arr[i]
        res.append(maximum)
    i-=1
j= len(res)-1
for i in arr:
    if i ==res[j]:
        j-=1
    result.append(res[j])
print(result)




arr = [17,18,8,4,6,1]



temp = []
temp+=arr
res = []

for i in arr:
    print(i)
    temp.remove(temp[0])
    if len(temp) !=0:
        res.append(max(temp))
    else:
        res.append(-1)

print(res)


s = "abc"
t = "ahbgdc"
# for i 

arr = [17,18,5,4,6,1]
arr =[400]
maximum =-1
i = len(arr)-1
while i >=0:
    if arr[i] > maximum:
        new_maximum = arr[i]
    arr[i] = maximum
    maximum = new_maximum
    i-=1
print(arr)

s = "abc"
t = "ahbgdc"
# s ="aaaaaa"
# t ="bbaaaa"
# s ="ab"
# t ="baab"
# s ="axc"
# t ="ahbgdc"
j =0
for i in t:
    if i == s[j]:
        if j+1 <len(s):
            j+=1
            print(j)
        else:
            print('true')
    
temp=[]
for i in s:
    if i in t:
        index = t.index(i)
        temp.append(index)
        print(i)
        #remove the letter from t
        t = t.replace(i,'',1)
        print(t)
    else:
        print('false')

print(temp)
if temp == sorted(temp):
    print('true')

def perfect(num,i,memo={}):
    if i in memo:
        print('used')
        return memo[i]
    sumation = 0
    if i == 0:
        return 0
    if num%i==0:
        sumation = i
    memo[i]=sumation + perfect(num,i-1,memo)
    return memo[i]
    

# num =2096128
num =28
print(perfect(2096128,2096128//2))
sumofnum = perfect(28)
if sumofnum == num:
    print('true')
else:
    print('false')

emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
temp = []
for i in emails:
    print(i)
    local_name = i.split('@')[0]
    domain_name = i.split('@')[1]
    local_name = local_name.split('+')[0]
    local_name = local_name.replace('.','')
    i = local_name+'@'+domain_name
    if i not in temp:
        temp.append(i)
print(len(temp))

encoded = [1,2,3]
first = 1
encoded = [6,2,7,3]
first = 4
arr = [first]
i = 0
while i < len(encoded):
    print(encoded[i])
    j = encoded[i] ^ arr[i]
    arr.append(j)
    i+=1

print(arr)

nums = [1,2,3,4,0]
index = [0,1,2,3,0]
target = []
i = 0
while i < len(nums):
    target.insert(index[i],nums[i])
    i+=1
print(target)
flowerbed = [1,0,0,0,1]
n = 1
flowerbed = [1,0,0,0,0,0,1]
n = 2
flowerbed =[1,0,0,0,0,1]
n = 2
flowerbed =[1,0,1,0,1,0,1]
flowerbed =[0,0,1,0,1]
n=1
flowerbed =[1,0,0,0,1,0,0]
n=2
flowerbed =[1,0,0,0,1]
n=2
flowerbed=[0,0]
n=2
prev = 0
counter =0
i=0
while i< len(flowerbed):
    # print(i)
    # if i == len(flowerbed)-1 and prev == 0 and flowerbed[i] ==0:
    #     print('hi',i,flowerbed[i])
    #     counter+=1
    if i+1 < len(flowerbed):
        if prev== 0 and flowerbed[i] ==0 and flowerbed[i+1] ==0:
            counter +=1
            prev = 1
        # print(flowerbed[i],flowerbed[i+1],prev)
        # if flowerbed[i+1]==0  and flowerbed[i]!=1 and prev == 0:
        #     counter +=1
        #     prev = 1
        #     print('possible')
        else:
            prev = flowerbed[i]
    
    i+=1
if counter >= n:
    print('true')
else:
    print('flase')

chars = ["a","a","b","b","c","c","c"]
# chars = ["a"]
chars =["a","b","b","b","b","b","b","b","b","b","b","b","b"]
chars.append('test')
i = 0
prev = None
temp_count = 0
k = len(chars)
while i < k:
    chars.remove(chars[i])
    k-=1
    if chars[i]== prev:
        if temp_count > 0:
            chars.remove(chars[i])
        temp_count+=1
    else:
        if temp_count !=0:
            chars[i] = temp_count
        temp_count=0
    prev = chars[i]
    i+=1
print(chars,temp_count)


















chars.append('test')
res = []
prev = chars[0]
temp_count = 0
for i in chars:
    if temp_count == 0:
        res.append(i)
        temp_count+=1
    print(prev,i)
    if prev == i:
        temp_count+=1
        print(temp_count)
    else:
        if temp_count >9:
            temp_count = str(temp_count)
            for j in temp_count:
                #append the number to res with double quotes
                res.append(j)
            temp_count = 0
        else:
            res.append(str(temp_count))
            temp_count = 0
        print(temp_count)
    if i == "test":
        break
    prev = i

print(res)
pattern = "egg"
k = "add"

pattern = "abba"
s = "dog cat cat dog"
pattern = "aaaa"
s = "dog cat cat dog"
k =s.split(' ')
s = "foo"
t = "bar"
pat ={}
st = {}
if len(s) == len(t) :
    i = 0
    while i < len(s):
        if s[i] in pat and pat[s[i]] != t[i]:
            print('false')
        if t[i] in st and st[t[i]]  != s[i]:
            print('false') 
        pat[s[i]] = t[i]
        st[t[i]] = s[i]
        i+=1
    print(pat)
    print(st)
else:
    print('False')
print('True')

k = 5
count = 0
i =1
while i <1001:
    if i-1 < len(arr):
        print(arr[i-1],'---',i)
        if arr[i-1] != i:
            print(i)
    i+=1
for i in range(1,1001):
    if i-1< len(arr):
        # print(arr[i-1])
        if arr[i-1] != i:
            count+=1
            print(count)
    print(i)
    if count == k:
        print(i)
        break

arr = [2,3,4,7,11]
# for i in arr:
    
# nums = [1,2,3,4,5]
left = 1
right = 1
i = 0
while i < len(nums):
    prev = len(nums)- i
    print(prev)
    post = (i+1)-len(nums)
    print(post)

    i+=1

arr = [4,3,1,1,3,3,2]
k = 3
temp = {}
i =0
while i < len(arr):
    if arr[i] not in temp:
        temp[arr[i]] = arr.count(arr[i])
    i+=1
print(temp)
for j in temp:
    print(j)
print(sum(temp))
temp = sorted(temp)
print(temp)

def isMatch(s: str, p: str) -> bool:
    n, m = len(s), len(p)
    dp = [[False] * (m+1) for _ in range(n+1)]
    dp[0][0] = True
    for i in range(1, n+1):
        dp[i][0] = False
    for j in range(1, m+1):
        if p[j-1] == '*' and dp[0][j-2]:
            dp[0][j] = True
        elif p[j-1] == '*':
            dp[0][j] = dp[0][j-2]
        else:
            dp[0][j] = False
    for i in range(1, n+1):
        for j in range(1, m+1):
            if s[i-1] == p[j-1] or p[j-1] == '.':
                dp[i][j] = dp[i-1][j-1]
            elif p[j-1] == '*':
                dp[i][j] = dp[i][j-2]
                if s[i-1] == p[j-2] or p[j-2] == '.':
                    dp[i][j] |= dp[i-1][j]
            else:
                dp[i][j] = False
    return dp[n][m]

print(isMatch("aa","a*"))