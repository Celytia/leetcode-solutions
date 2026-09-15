class Solution:
    def reverseWords(self, s: str) -> str:
        words=[]
        word=""
        for i in s:
            if i!=" ":
                word+=i
            else:
                if word:
                    words.append(word)
                    word=""
        if s[-1]!=" ":
            words.append(word)
        result=""
        for i in range(len(words)-1,-1,-1):
            result+=words[i]+" "
        result=result[:-1]
        return result