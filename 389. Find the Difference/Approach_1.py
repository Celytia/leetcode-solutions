class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        letter = [0] * 26
        for i in range(len(s)):
            if s[i] in t:
                letter[ord(s[i]) - ord("a")] +=1
        for i in range(len(t)):
            if letter[ord(t[i]) - ord("a")] == 0:
                return t[i]
            letter[ord(t[i]) - ord("a")]-=1