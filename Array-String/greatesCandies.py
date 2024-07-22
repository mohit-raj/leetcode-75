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
    

# Main code to test the function
if __name__ == "__main__":
    solution = Solution()
    candies = [2, 3, 5, 1, 3]
    extraCandies = 3
    result = solution.kidsWithCandies(candies, extraCandies)
    print(result)  # Output should be [True, True, True, False, True]
