class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dict = {}
        a = 0
        length = 0
        list1 = []
        i=0
        while s:
            try:
                if s[i] not in list1:
                    list1.append(s[i])
                    dict[a] = list1

                    i+=1
                else:
                    s=s.lstrip(s[0])
                    a += 1
                    list1 = []
                    i = 0
            except IndexError:
                break


        for x in dict.values():
            if length < len(x):
                length = len(x)
        return length
a=Solution()
print(a.lengthOfLongestSubstring('ab'))


# class Solution:
#     # @return an integer
#     def lengthOfLongestSubstring(self, s):
#         start = maxLength = 0
#         usedChar = {}
#
#         for i in range(len(s)):
#             if s[i] in usedChar and start <= usedChar[s[i]]:
#                 start = usedChar[s[i]] + 1
#             else:
#                 maxLength = max(maxLength, i - start + 1)
#
#             usedChar[s[i]] = i
#
#         return maxLength