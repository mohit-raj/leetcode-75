from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        iCandidate = float('inf')
        jCandidate = float('inf')
        for num in nums:
            if(num <= iCandidate):
                iCandidate = num
            elif(num <= jCandidate):
                jCandidate = num
            else:
                return True
        return False
        
        