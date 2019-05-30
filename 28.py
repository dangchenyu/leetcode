class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack == "" and needle == "":
            return 0
        elif haystack == "" and needle != "":
            return -1
        elif needle == "":
            return 0

        for i in range(len(haystack) - len(needle) + 1):
            for j in range(len(needle)):
                if haystack[i +j] == needle[j]:
                    if j == len(needle) - 1:
                        return i
                    else:
                        continue
                else:
                    break
        return -1

s=Solution()
print(s.strStr("mississippi",'sippi'))