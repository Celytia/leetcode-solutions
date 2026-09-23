class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in s:
            if i=="(" or i=="[" or i=="{":
                stack.append(i)
            elif not stack: 
                return False
            else:
                top=stack.pop()
                if not(top=="(" and i==")" or top=="[" and i=="]" or top=="{" and i=="}" ):
                    return False
        return len(stack)==0