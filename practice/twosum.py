# nums = [3,2,4]
# target = 6

# #sort the list
# nums.sort()
# print(nums)
# # create two pointers, one at the beginning and one at the end
# i = 0
# j = len(nums)-1
# # while the two pointers don't overlap
# while i < j:
#     # if the sum of the two pointers is equal to the target, return the indices
#     if nums[i] + nums[j] == target:
#         print(i,j)
#         break
#     # if the sum of the two pointers is less than the target, move the left pointer up
#     elif nums[i] + nums[j] < target:
#         i+=1
#     # if the sum of the two pointers is greater than the target, move the right pointer down
#     elif nums[i] + nums[j] > target:
#         j-=1
# # if the two pointers overlap, return an error message
# else:
#     print("No two sum solution")


def two_sum(nums, target):
    # Sort the array
    nums.sort()

    # Initialize two pointers, one at the beginning and one at the end
    left, right = 0, len(nums) - 1

    while left < right:
        current_sum = nums[left] + nums[right]
        print(current_sum)
        print(nums[left])
        print(nums[right])

        if current_sum == target:
            # Return the indices of the two numbers that add up to the target
            return [left, right]
        elif current_sum < target:
            # If the sum is less than the target, move the left pointer to the right
            left += 1
        else:
            # If the sum is greater than the target, move the right pointer to the left
            right -= 1

    # If no solution is found, return an empty list or raise an exception
    return []

# Example usage:
nums = [2,3,4]
target = 6
result = two_sum(nums, target)
print(result)


# THIS CODE DOESN'T WORK ON LEETCODE BECAUSE IT USES SORTING SO THE INDICES ARE MESSED UP