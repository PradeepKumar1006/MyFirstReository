class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0
        l = 0

        for r in range(len(chars) + 1):

            if r == len(chars) or chars[r] != chars[l]:

                chars[write] = chars[l]
                write += 1

                count = r - l

                if count > 1:
                    for digit in str(count):
                        chars[write] = digit
                        write += 1

                l = r

        return write