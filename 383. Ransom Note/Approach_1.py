class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for i in ransomNote:
            if i not in magazine:
                return False
            else:
                for j in range(len(magazine)):
                    if i==magazine[j]:
                        if j==0:
                            magazine=magazine[1:]
                        else:
                            magazine=magazine[:j]+magazine[j+1:]
                        break
        return True 