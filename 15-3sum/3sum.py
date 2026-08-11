class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
        nums.sort() # sort the array
        result = [] # where your results go
        target = 0
        for i in range(len(nums)):
            if nums[i] > 0: # if the first number is positive, immediately stop because the array is sorted an all numbers are positive
                break
            if i > 0 and nums[i] == nums[i-1]: # so it doesn't compare to the last element of the array
                continue 
            left = i + 1
            right = len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right] # add up the 3 numbers, one index, left, right
                if total == target: # if the total is equal to the target, append to the array
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1 # move left up 1
                    right -= 1 # move right down 1
                    while left < right and nums[left] == nums[left-1]: # if theres a duplicate, move up left by 1
                        left += 1
                elif total < target: # if the total is less than the target, move left by 1
                    # you do this because if the total is less than the target, you want to increase your total value 
                    left += 1
                else: # else you move right closer
                    right -= 1
        return result
            