class Solution:
    def reverse(self, x: int) -> int:

        sign = -1 if x < 0 else 1

        x = abs(x)

        z = ""

        while x > 0:
            z += str(x % 10)
            x //= 10

        if z == "":
            return 0

        ans = sign * int(z)

        if ans < -2**31 or ans > 2**31 - 1:
            return 0

        return ans