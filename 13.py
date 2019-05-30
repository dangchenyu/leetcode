class Solution:
    def romanToInt(self, s: str) -> int:
        dt = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90,
              'CD': 400, 'CM': 900}
        sum = 0
        i=0
        while i<=len(s):
            try:
                if s[i] + s[i + 1] in dt.keys():

                    temp=dt[s[i] + s[i + 1]]
                    sum = sum + temp
                    if i+2<len(s):
                        i=i+2
                    else:
                        break
                else:
                    sum = sum + dt[s[i]]
                    i = i + 1
            except:
                sum = sum + dt[s[i]]
                temp1=dt[s[i]]
                break
        return sum
s=Solution()
print(s.romanToInt("IV"))
class Solution:

    def romanToInt(self, s):
        roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
        z = 0
        for i in range(0, len(s) - 1):
            if roman[s[i]] < roman[s[i+1]]:
                z -= roman[s[i]]
            else:
                z += roman[s[i]]
        return z + roman[s[-1]]