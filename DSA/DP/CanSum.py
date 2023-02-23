#can sum with out dynamic programing
def cansum(target,num):
    if target == 0:
        return True
    if target<0:
        return False
    for i in num:
        remainder = target-i
        if cansum(remainder,num) == True:
            return True
    return False
print(cansum(7,[2,4,5,3,2,1,4]))
# print(cansum(300,[7,14]))

#can sum with dp
def cansumdp(target,num,memo={}):
    if target in memo:
        return memo[target]
    if target == 0:
        return True
    if target <0:
        return False
    for i in num:
        remainder = target-i
        if cansumdp(remainder,num,memo) == True:
            memo[target] = True
            return True
    memo[target]= False
    return False

print(cansumdp(300,[7,14]))