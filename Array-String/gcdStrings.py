import math
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        smallStr, bigStr = (str1, str2) if len(str1) < len(str2) else (str2, str1)
        lenGCD = math.gcd(len(smallStr), len(bigStr))
        resultStr = smallStr[:lenGCD]
 
        i, j = 0, 0
        while(j < len(bigStr) and i < len(resultStr)):
            if(bigStr[j] == resultStr[i]):
                i += 1
                j += 1
                if(i == len(resultStr)):
                    i = 0
            else:
                resultStr = ""
                break

        i, j = 0, 0
        while(j < len(smallStr) and i < len(resultStr)):
            if(smallStr[j] == resultStr[i]):
                i += 1
                j += 1
                if(i == len(resultStr)):
                    i = 0
            else:
                resultStr = ""
                break
           
        return resultStr
            


        
        


        