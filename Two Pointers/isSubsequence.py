class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if(t == "" and s != ""):
            return False
        elif(t == "" and s == ""):
            return True
        elif(t != "" and s == ""):
            return True
        else:
            j, checkSubseq = 0, 0
            while(j < len(t)):
                if(t[j] == s[checkSubseq]):
                    checkSubseq += 1
                    j += 1
                else:
                    j += 1
    
                if(checkSubseq == len(s)):
                    return True
        return False
        
# Main code to test the function
if __name__ == "__main__":
    solution = Solution()
    s = "b"
    t = "abc"
    val = solution.isSubsequence(s, t)
    print (val)
        