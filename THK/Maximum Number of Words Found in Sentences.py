sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
count = 0
for i in sentences:
    j =i.split(' ')
    count = len(j)
    if len(j) > count:
        count = len(j)
print(count)