class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        s=""
        while columnNumber!=0:
            if columnNumber%26==0:
                s="Z"+s
                columnNumber=columnNumber//26-1
            else:
                s=chr(columnNumber%26+ord("A")-1)+s
                columnNumber=columnNumber//26
        return s