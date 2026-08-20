class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if num%10!=0 or num==0:
            return True
        else:
            return False