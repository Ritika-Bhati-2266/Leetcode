class Solution:
    def isThree(self, n: int) -> bool:
        c=0
        i=1
        while i<=n:
            if n%i==0:
                c=c+1
            i=i+1
        if c==3:
            return True
        else:
            return False