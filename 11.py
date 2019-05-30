class Solution:
    def maxArea(self, height) -> int:
        opt_max=0
        i=0
        length=len(height)
        while i <length-1:
            if height[i] < opt_max/(length-i-1):
                i=i+1
                continue
            idx=0
            j=i+1
            while j<length:
                if height[j+1]>height[j]:
                    j+=1
                    continue
                if height[i]>=height[j]:
                    opt= height[j]*(j-i)
                else:
                    opt=height[i]*(j-i)
                if opt_max<opt:
                    opt_max=opt
                j+=1
            i=i+1
        return opt_max
s=Solution()

def maxArea(self, height):
    L, R, width, res = 0, len(height) - 1, len(height) - 1, 0
    for w in range(width, 0, -1):
        if height[L] < height[R]:
            res, L = max(res, height[L] * w), L + 1
        else:
            res, R = max(res, height[R] * w), R - 1
    return res