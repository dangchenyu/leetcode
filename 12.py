class Solution:
    def intToRoman(self, num: int) -> str:
        opt=''
        i=len(str(num))
        while i>0:
            reminder=num//(10**(i-1))
            if i==1:
                if reminder<4:
                    alp= 'I'*reminder
                if reminder==4:
                    alp='IV'
                if reminder==9:
                    alp='IX'
                if reminder>=5 and reminder!=9:
                    alp='V'+reminder%5*'I'
            if i==2:
                if reminder<4:
                    alp= 'X'*reminder
                if reminder==4:
                    alp='XL'
                if reminder==9:
                    alp='XC'
                if reminder>=5 and reminder!=9:
                    alp='L'+reminder%5*'X'
            if i==3:
                if reminder<4:
                    alp= 'C'*reminder
                if reminder==4:
                    alp='CD'
                if reminder==9:
                    alp='CM'
                if reminder>=5 and reminder!=9:
                    alp='D'+reminder%5*'C'
            if i==4:
                    alp=reminder*'M'
            opt=opt+alp
            num=num%(10**(i-1))
            i-=1
        return opt
s=Solution()
print(s.intToRoman(3379))

class Solution(object):
    def intToRoman(self, num):
        dict = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        result = ""
        for letter, n in zip(dict, nums):
            result += letter * int(num / n)
            num %= n
        return result