# nums = [1,2,3,1]
# nums= [2,7,9,3,1]
# nums = [2,1,1,2]
# nums = [1,2,3,4,5,6]
nums = [1,2,3,1]
length = len(nums)
previ= 0
prevj=0
even_max = 0
odd_max = 0
i=0
# j = length-1
while i < length:
    if i+1 < length:
        j = i+1
        # print(j-i)
        print(previ,'previ',prevj,'prevj')
        print(nums[i],'i')
        if odd_max + prevj > odd_max + nums[i] and i-(j-1) != 1:
            odd_max += prevj
        else:
            odd_max +=nums[i]
        # print(odd_max,'i max')
        previ = nums[i]
        print(nums[j],'j')
        if even_max +previ > even_max + nums[j] and j-(i-1) != 1:
            even_max +=previ
        else:
            even_max += nums[j]
        # print(even_max,'j max')
        prevj = nums[j]

    i+=2
# print(even_max,odd_max)
if even_max > odd_max:
    print(even_max)
else:
    print(odd_max)
