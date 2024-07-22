from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        availablePos = []
        while(i < len(flowerbed)):
            if(not flowerbed[i]):
                availablePos.append(i)
            i += 1
        
        for i in availablePos:
            if(n):
                if(i > 0 and i < (len(flowerbed) - 1)):
                    if(flowerbed[i-1] != 1 and flowerbed[i+1] != 1):
                        flowerbed[i] = 1
                        n -= 1
                else:
                    if(i == 0):
                        if(len(flowerbed) > 1):
                            if(flowerbed[i+1] != 1):
                                flowerbed[i] = 1
                                n -= 1
                        else:
                            if(not flowerbed[i]):
                                flowerbed[i] = 1
                                n -= 1
                    else:
                        if(flowerbed[i-1] != 1):
                            flowerbed[i] = 1
                            n -= 1
        
        return False if n else True
