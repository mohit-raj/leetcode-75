from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forwardCumProd = []
        backwardCumProd = []
        n = len(nums)
        resultantProd = [1] * n
        
        temp = 1
        for i in range(len(nums)):
            temp *= nums[i]
            forwardCumProd.append(temp)

        temp = 1
        i = len(nums) - 1
        while(i > -1):
            temp *= nums[i]
            backwardCumProd.append(temp)
            i -= 1

        backIndex = n-2
        for i in range(len(nums)):
            if(i == 0):
                resultantProd[i] = backwardCumProd[backIndex]
                backIndex -= 1
            elif(i == n-1):
                resultantProd[i] = forwardCumProd[i-1]
            else:
                resultantProd[i] = forwardCumProd[i-1] * backwardCumProd[backIndex]
                backIndex -= 1
        
        return resultantProd
        