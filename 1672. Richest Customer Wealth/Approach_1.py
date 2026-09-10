class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        arr=[0]*len(accounts)
        for i in range(len(accounts)):
            for j in range(len(accounts[i])):
                arr[i]+=accounts[i][j]
        max=0
        for i in range(len(arr)):
            if arr[i]>=max:
                max=arr[i]
        return max