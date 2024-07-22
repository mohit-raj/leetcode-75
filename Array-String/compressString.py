from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        s = ""
        countChar = 1
        i = 1
        while(i < len(chars)):
            if(chars[i-1] == chars[i]):
                countChar += 1
            else:
                s += chars[i-1]
                if countChar > 1:
                    s += str(countChar)
                countChar = 1 
            i += 1
        
        s += chars[i-1]
        if countChar > 1:
            s += str(countChar)
        
        for j in range(len(s)):
            chars[j] = s[j]        
            
        return len(s)

