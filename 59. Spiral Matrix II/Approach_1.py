class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        m=[[0]*n for _ in range(n)]
        s=1
        i=j=0
        top,bottom,l,r=0,n-1,0,n-1
        while top<=bottom and l<=r:
            for i in range(l,r+1):
                m[top][i]=s
                s+=1
            top+=1
            for i in range(top,bottom+1):
                m[i][r]=s
                s+=1
            r-=1
            if top<=bottom:
                for i in range(r,l-1,-1):
                    m[bottom][i]=s
                    s+=1
                bottom-=1
            if l<=r:
                for i in range(bottom,top-1,-1):
                    m[i][l]=s
                    s+=1
                l+=1
        return m