def three_sum(nums, target):
    result = []
    nums.sort()

    for i in range(len(nums) - 2):
        # Skip duplicates for the first element in the triplet
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, len(nums) - 1

        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]

            if current_sum == target:
                result.append([nums[i], nums[left], nums[right]])

                # Skip duplicates for the second element in the triplet
                while left < right and nums[left] == nums[left + 1]:
                    left += 1

                # Skip duplicates for the third element in the triplet
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1

            elif current_sum < target:
                left += 1
            else:
                right -= 1

    return result

# Example usage:
nums = [-1, 0, 1, 2, -1, -4]
target = 0
result = three_sum(nums, target)
print(result)