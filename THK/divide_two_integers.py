import math
dividend = 7
divisor = -3
quotient = dividend/divisor
if quotient > 0:
    quotient = math.floor(quotient)
else:
    quotient = math.ceil(quotient)

if quotient > 2147483647:
    quotient = 2147483647
elif quotient < -2147483648:
    quotient = -2147483648

print(quotient)