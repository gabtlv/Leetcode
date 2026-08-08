class Solution(object):
    def twoSum(self, nums, target):
        checked = {}
        for i in range(len(nums)):
            remainder = target - nums[i]
            if remainder in checked:
                return [checked[remainder], i]
            checked[nums[i]] = i
        