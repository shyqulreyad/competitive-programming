s = "Let's take LeetCode contest"
s = "God Ding"
res =''
x = s.split()
for idx, i in enumerate(x):
    if idx == 0:
        res+=i[::-1]
    else:
        res+= ' '+i[::-1]
print(res)