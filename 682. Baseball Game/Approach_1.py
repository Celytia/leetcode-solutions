class Solution:
    def calPoints(self, operations: List[str]) -> int:
        s=[]
        i=0
        while i<len(operations):
            if operations[i]=="C":
                s.pop()
            elif operations[i]=="+":
                s.append(str(int(s[-1])+int(s[-2])))
            elif operations[i]=="D":
                s.append(str(int(s[-1])*2))
            else:
                s.append(operations[i])
            i+=1
        rec=0
        for i in range(len(s)):
            if s[i]!="":
                rec+=int(s[i])
        return rec