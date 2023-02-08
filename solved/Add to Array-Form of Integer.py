num =[1,2,6,3,0,7,1,7,1,9,7,5,6,6,4,4,0,0,6,3]
k = 516
s = [str(integer) for integer in num]
a_string = "".join(s)
res = int(a_string)
result = [int(x) for x in str(res+k)]
print(result)