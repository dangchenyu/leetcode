class Solution:
    def reverse(self, x: int) -> int:

            if x<0:
                return (-int(str(abs(x))[::-1]) if int(str(abs(x))[::-1]) < pow(2, 31)  else 0)
            else:
                return (int(str(x)[::-1]) if int(str(x)[::-1]) < pow(2, 31)  else 0)