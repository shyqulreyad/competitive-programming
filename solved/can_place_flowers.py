def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
    prev = 0
    counter =0
    flowerbed.append(0)
    i=0

    while i< len(flowerbed):
        if i+1 < len(flowerbed):
            if prev== 0 and flowerbed[i] ==0 and flowerbed[i+1] ==0:
                counter +=1
                prev = 1
            else:
                prev = flowerbed[i]
        i+=1
    if counter >= n:
        return True
    else:
        return False