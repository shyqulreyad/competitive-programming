prices = [1,2,3,4,5,1,10]
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