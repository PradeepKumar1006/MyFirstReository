class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            temp = n
            dp = 1

            while temp:
                dp *= temp % 10
                if product == 0:
                    break
                temp //= 10

            if dp % t == 0:
                return n

            n += 1