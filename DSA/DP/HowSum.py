#how sum with out dp
# def howsum(target,nums):
#     if target == 0:
#         return []
#     if target<0:
#         return None
#     for i in nums:
#         remainder = target -i
#         res = howsum(remainder,nums)
#         if res != None:
#             return [*res,i]
#     return None

# print(howsum(7,[2,4]))
#how sum with dp
def howsumdp(target,nums,memo={}):
    if target in memo:
        return memo[target]
    if target == 0:
        return []
    if target<0:
        return None
    for i in nums:
        remainder = target -i
        res = howsumdp(remainder,nums,memo)
        if res != None:
            memo[target] = [*res,i]
            # print(memo)
            return [*res,i]
    memo[target] = None
    return None

# print(howsumdp(300,[7,14]))
print(howsumdp(7,[2,3,6,7]))