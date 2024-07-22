class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

        toReverse = []
        for i in s:
            if(i in vowels):
                toReverse.append(i)

        n = len(toReverse)
        for i in range(0, len(s)):
            if(s[i] in vowels and n > 0):
                s[i] = toReverse[n-1]
                n -= 1

        resultStr = ""
        for element in s:
            resultStr += str(element)
        return resultStr