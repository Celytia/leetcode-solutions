class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m=len(word1)
        n=len(word2)
        a=""
        if m>n:
            for i in range(n):
                a+=word1[i]+word2[i]
            for i in range(n,m):
                a+=word1[i]
        else:
            for i in range(m):
                a+=word1[i]+word2[i]
            for i in range(m,n):
                a+=word2[i]
        return a