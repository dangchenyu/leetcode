class Solution:

    def longestPalindrome1(self, s, dict1=None):

        self.dic=dict1
        if self.dic is None:
            self.dic = {}
        self.list1 = []
        for i in s:
            if i not in s[1:] and self.list1 == []:

                s = s[1:]

                continue
            else:
                if i not in self.list1:
                    self.list1.append(i)
                else:
                    self.list1.append(i)
                    self.dic[len(s)] = self.list1
                    self.list=[]
                    s = s[1:]
        if s:
            return self.longestPalindrome1(s, self.dic,)
        else:
            length = 0
            if self.dic:
                for x in self.dic.values():
                    if len(x) > length:
                        list_opt = ''.join(x)
                        return list_opt
            else:
                if self.str_opt:
                    return self.str_opt
                else:
                    return ""


    def longestPalindrome(self, s):
        self.str_opt = s[0] if s else ""

        if len(s) == 1:
            return s
        else:
            return self.longestPalindrome1(s, None)

a=Solution()
print(a.longestPalindrome("aabbb"))

class Solution:

    def longestPalindrome(self, s):
        if len(s)==0:
            return ""
        maxLen=1
        start=0
        for i in range(len(s)):
            if i-maxLen >=1 and s[i-maxLen-1:i+1]==s[i-maxLen-1:i+1][::-1]:
                start=i-maxLen-1
                maxLen+=2
                continue

            if i-maxLen >=0 and s[i-maxLen:i+1]==s[i-maxLen:i+1][::-1]:
                start=i-maxLen
                maxLen+=1
        return s[start:start+maxLen]