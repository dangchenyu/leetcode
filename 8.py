class Solution:
    def myAtoi(self, str: str) -> int:
        str1 = str.lstrip()
        l = []

        for i in str1:
            try:
                if i=="0":
                    l.append(i)
                elif int(i):
                    l.append(i)
            except:
                if i == "-" and l == []:
                    l.append(i)
                elif i == "+" and l == []:
                    l.append(i)
                else:
                    break
        s = ''.join(l)
        if s and s != "-" and s !="+":
            if int(s) < -2 ** 31:
                return -2 ** 31
            elif int(s) >= 2 ** 31:
                return 2 ** 31-1
            else:
                return int(s)

        else:
            return 0
s=Solution()
print(s.myAtoi(
"010"))