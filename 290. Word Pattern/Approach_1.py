class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s=s.split()
        if len(pattern)!=len(s):
            return False
        dic={}
        for i in range(len(pattern)):
            if pattern[i] not in dic:
                if s[i] in dic.values():
                    return False
                else:
                    dic[pattern[i]]=s[i]
            else:
                if dic[pattern[i]]!=s[i]:
                    return False
        return True