class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
      x=0
      while 2**x<n:
        x+=1
      if 2**x==n:
        return True
      return False  