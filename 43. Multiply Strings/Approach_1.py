class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        result=[0]*(len(num1)+len(num2))
        for i in range(len(num1)-1,-1,-1):
            d1=ord(num1[i])-ord("0")
            for j in range(len(num2)-1,-1,-1):
                d2=ord(num2[j])-ord("0")
                sum=d1*d2+result[i+j+1]
                result[i+j+1]=sum%10
                result[i+j]+=sum//10
        op=""
        flag=True
        for i in range(len(result)):
            if result[i]!=0 or not flag:
                op+=str(result[i])
                flag=False
        return op