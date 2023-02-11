grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
counter =0
for i in grid:
    for j in i:
        if j < 0:
            counter+=1
print(counter)