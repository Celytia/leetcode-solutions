class Solution:
    def maxFreqSum(self, s: str) -> int:
        dic={"a":0,"e":0,"i":0,"o":0,"u":0}
        lst=[0]*26
        for i in s:
            if i in dic:
                dic[i]+=1
            else:
                lst[ord(i)-ord("a")]+=1
        return dic[max(dic,key=dic.get)]+max(lst)