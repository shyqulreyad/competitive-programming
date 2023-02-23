#how sum with out dp
def howsum(target,nums):
    if target == 0:
        return []
    if target<0:
        return None
    for i in nums:
        remainder = target -i
        res = howsum(remainder,nums)
        if res != None:
            return [*res,i]
    return None

print(howsum(7,[2,4]))