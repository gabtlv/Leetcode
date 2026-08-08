class Solution(object):
    def containsDuplicate(self, nums):
        # if any value appears at least twice, return true
        # make another array, sort it, then compare with original
        sortedNums = sorted(nums)
        for i in range(len(sortedNums) - 1):
            if sortedNums[i] == sortedNums[i+1]:
                return True
        return False
        