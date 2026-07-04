class Solution:
    def reverse(self, x: int) -> int:
        num = abs(x)
        sum = 0
        while num>0:
            l = num%10
            sum = sum*10+l
            num = num//10
        if x<0:
            sum = -sum
        if sum <-2**31 or sum >2**31-1:
            return 0
        return sum
