class Solution:
    def letterCombinations(self, digits: str):
        dict = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        list_alp = []
        result = []
        length = 1
        temp = 1
        if digits == '':
            return result
        for i in digits:
            if i in dict.keys():
                list_alp.append(dict[i])

        if result == []:
            for i in list_alp[0]:
                result.append(i)
            list_alp.pop(0)
        while len(result[0]) < len(digits):

            if list_alp != []:

                for k in list_alp[0]:

                    if len(result[0]) > length:
                        list_alp.pop(0)
                        break
                    temp = len(result)
                    result.append(result[0] + k)

                length = len(result[0])
                if len(result) != temp:
                    result.pop(0)

        return result