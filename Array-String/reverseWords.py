class Solution:
    def reverseWords(self, s: str) -> str:
        sToList = s.split(' ')
        space = 0
        for i in sToList:
            if(i == ''):
                space += 1

        reverseStr = ''
        i = len(sToList) - 1
        space = i-space
        while(i > -1):
            if(sToList[i] != ''):  
                reverseStr += sToList[i]
                if(space):
                    reverseStr += ' '
                    space -= 1
            i -= 1
              
        return reverseStr
