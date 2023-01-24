# prices = [7,1,5,3,6,4]
# prices = [7,6,4,3,1]
# prices = [1,2,3,4,5]
# prices =[3,3,5,0,0,3,1,4]
prices = [1,2,3,0,2]
prices =[1,2,4]

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
        max_profit = profit
        total +=profit
        min_price = prices[i]
        max_profit = 0
        i+=1
        # print(max_profit)
        # min_price = max(prices)
    i+=1
print(total)