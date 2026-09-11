# 43. Multiply Strings

### Difficulty: Medium

## Description
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

 
Example 1:
Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:
Input: num1 = "123", num2 = "456"
Output: "56088"

 
Constraints:


	1 <= num1.length, num2.length <= 200
	num1 and num2 consist of digits only.
	Both num1 and num2 do not contain any leading zero, except the number 0 itself.

## Submission Details
- **Status**: Accepted
- **Runtime**: N/A
- **Memory**: N/A
- **Language**: python3

## Code
```python3
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
```
