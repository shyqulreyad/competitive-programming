names = ["Mary","John","Emma"]
heights = [10,165,170]
res ={}
result = []
for i in range(len(names)):
    res[heights[i]] = names[i]
sorted_keys =sorted(res.keys(),reverse=True)
for i in sorted_keys:
    result.append(res[i])
print(result)