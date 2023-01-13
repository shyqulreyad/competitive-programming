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
def bin(n):
    if n > 1:
        bin(n//2)
    print(n % 2, end="")
bin(1534236469)
print()
bin(4)
