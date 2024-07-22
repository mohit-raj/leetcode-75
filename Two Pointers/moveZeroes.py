from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> List:
        """
        Do not return anything, modify nums in-place instead.
        """
        if(len(nums) > 2):
            i = 0
            j = 1
            while(j < (len(nums))):
                if(nums[i] != 0 and nums[j] == 0):
                    j += 1
                elif(nums[i] == 0 and nums[j] != 0):
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                    j += 1
                elif(nums[i] == 0 and nums[j] == 0):
                    j += 1
                else:
                    if(j - i > 1):
                        nums[i+1] = nums[j]
                        nums[j] = 0
                        i += 1
                        j += 1
                    else:
                        i += 1
                        j += 1
        elif(len(nums) == 1):
            return nums
        else:
            if(nums[0] == 0 and nums[1] != 0):
                nums[0], nums[1] = nums[1], nums[0]
                return nums
            else:
                return nums