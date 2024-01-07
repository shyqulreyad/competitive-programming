
def two_sum(nums, target):
    remainder = []
    for i in range(len(nums)):
        remain = target-nums[i]
        if (nums[i] in remainder):
            return (i,remainder.index(nums[i]))
        else:
            remainder.insert(i,remain)
        
# Example usage:
nums = [2,3,4]
target = 6
result = two_sum(nums, target)
print(result)
