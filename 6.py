class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows >= len(s) or numRows == 1:
            return s

        else:
            index = 0
            stride = 1
            opt = [''] * numRows

            for i in s:
                opt[index] += i
                if index == 0:
                    stride = 1
                if numRows - index == 1:
                    stride = -1
                index += stride
        return ''.join(opt)