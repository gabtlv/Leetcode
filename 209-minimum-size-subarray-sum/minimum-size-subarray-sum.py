class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        #sliding window approach
        left=0
        current_sum = 0
        min_length = 1000000 #we want to find the minimum length here. so make the initial value infinity.

        for right in range(len(nums)):
            current_sum += nums[right]
            while current_sum >= target:
                min_length = min(min_length, right - left + 1)
                current_sum -= nums[left]
                left += 1
        return min_length if min_length != 1000000 else 0