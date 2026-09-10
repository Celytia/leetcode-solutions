class Solution:
    def average(self, salary: List[int]) -> float:
        max=0
        min=1000000
        sum=0
        for i in range(len(salary)):
            if salary[i]>=max:
                max=salary[i]
            if salary[i]<=min:
                min=salary[i]
            sum+=salary[i]
        sum=sum-max-min
        return sum/(len(salary)-2)
