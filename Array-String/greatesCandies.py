from typing import List    
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxElement = max(candies)

        result = []
        for i in candies:
            if(i + extraCandies >= maxElement):
                result.append(True)
            else:
                result.append(False)  
        return result   
    

