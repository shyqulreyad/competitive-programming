# prices = [7,1,5,3,6,4]
# prices = [7,6,4,3,1]
# prices = [1,2,3,4,5]
# prices =[3,3,5,0,0,3,1,4]
# length = len(prices)
# min_price = max(prices)
# max_profit = 0
# total =[]
# i =0
# while i < length:
#     if prices[i] < min_price:
#         min_price = prices[i]
#     profit = prices[i]- min_price
#     print(prices[i],'---',min_price)
#     print(profit)
#     if profit > max_profit:
#         # print(profit)
#         max_profit = profit
#         total.append(profit)
#         min_price = prices[i]
#         max_profit = 0
#         i-=1
#         print(max_profit)
#         min_price = max(prices)
#     i+=1
# print(total)
# lenght = len(total)
# if lenght <=2:
#     print(sum(total),'hi')
# i = 0
# res = 0
# while i < lenght:
#     if i+1 <lenght:
#         prof = total[i]+total[i+1]
#         if prof > res:
#             res = prof
#     i+=1
# print(res,'res')


# prices = [1,2,3,4,5,1,10]
# prices = [7,6,4,3,1]
# prices = [3,3,5,0,0,3,1,4]
# # prices = [1,2,3,4,5]
# length = len(prices)
# min_price = max(prices)
# max_profit = 0
# max_array = []
# i =0
# while i < length:
#     if prices[i] < min_price:
#         min_price = prices[i]
#     profit = prices[i]- min_price
#     print(prices[i],'---',min_price,'===',profit)
#     if profit > max_profit:
#         print(profit)
#         # min_price = prices[i]
#         max_profit = profit
#         # max_array.append(max_profit)
#     i+=1
# print(max_array)
prices = [7,6,4,3,1]
prices = [1,2,3,4,5]
# prices =[3,3,5,0,0,3,1,4]
# prices =[3,3,5,0,0,3,1,4]
prices = [1,3,7,5,10,3]

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
    if profit > max_profit:
        print(profit)
        max_profit = profit
        total +=profit
        min_price = prices[i]
        max_profit = 0
        i-=1
        # print(max_profit)
        # min_price = max(prices)
    i+=1
print(total)