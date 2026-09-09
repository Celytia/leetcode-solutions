class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        n=len(arr)
        max=min=arr[0]
        for i in range(n):
            if arr[i]<min:
                min=arr[i]
            if arr[i]>max:
                max=arr[i]
        d=(max-min)/(n-1)
        for i in range(n):
            if min+i*d not in arr:
                return False
        return True