class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
        nums.sort() # sort the array
        result = [] # where your results go
        target = 0
        for i in range(len(nums)):
            if nums[i] > 0: # if the first number is positive, immediately stop because the array is sorted an all numbers are positive
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == target:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                elif total < target:
                    left += 1
                else:
                    right -= 1
        return result
            