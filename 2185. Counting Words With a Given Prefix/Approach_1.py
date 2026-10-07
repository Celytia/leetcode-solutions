class Solution:
    def prefixCount(self, words: list[str], pref: str) -> int:
        cnt=0
        for i in words:
            if pref not in i:
                continue
            if pref==i[:len(pref)]:
                cnt+=1
        return cnt