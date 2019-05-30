class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = 0
        list1 = nums[:]
        for x in nums:
            list1.remove(x)
            for y in list1:
                sum = x + y
                if sum == target:
                    break
            if sum == target:
                break
        if x != y:
            idx = [nums.index(x), nums.index(y)]
        else:
            list2 = nums[:]
            list2[nums.index(x)] = y + 1
            idx = [nums.index(x), list2.index(y)]
        return idx

def twoSum(self,nums, target):
    if len(nums) < 2:
        pass
    tempDict = {nums[0] : 0}
    for i in range(1, len(nums)):
        checkNum = target-nums[i]
        if(checkNum in tempDict.keys()):
            return [i,tempDict[checkNum]]
        else:
            tempDict[nums[i]] = i