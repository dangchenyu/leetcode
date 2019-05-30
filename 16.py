class Solution:
    def threeSumClosest(self, nums,target) :
        nums.sort()
        length = len(nums)
        result = nums[0] + nums[1] + nums[2]
        for i in range(0, length - 2):
            l, r = i + 1, length - 1
            while l<r:
                sum = nums[i] + nums[r] + nums[l]
                if sum == target:
                    return sum
                if abs(sum - target) < abs(result - target):
                    result = sum
                if sum > target:
                    r -= 1
                if sum < target:
                    l += 1

        return result
s=Solution()
print(s.threeSumClosest([1,2,4,8,16,32,64,128],82))