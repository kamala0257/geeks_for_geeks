
class Solution:
    def posInfinite(self, s, pos):
        n = len(s)

        while pos > n:
            length = n
            i = 1

            while length < pos:
                length = 2 * length + i
                i += 1

            previous_length = (length - i) // 2

            if pos > previous_length:
                if pos <= previous_length + i:
                    return '$'

                pos = length - pos + 1

        return s[pos - 1]
