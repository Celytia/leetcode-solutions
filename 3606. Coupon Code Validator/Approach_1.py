class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        ans=[]
        dic={"electronics":[], "grocery":[], "pharmacy":[],"restaurant":[]}
        for i in range(len(code)):
            if code[i] and all(c.isalnum() or c == "_" for c in code[i]) and isActive[i] and businessLine[i] in ["electronics", "grocery", "pharmacy", "restaurant"]:
                dic[businessLine[i]].append(code[i])
        for i in ["electronics", "grocery", "pharmacy", "restaurant"]:
            if dic[i]:
                ans.extend(sorted(dic[i]))
        return ans