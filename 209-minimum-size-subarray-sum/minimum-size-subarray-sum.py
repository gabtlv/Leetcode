class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        #sliding window approach
        #nums = [2,3,1,2,4,3]
        left = 0
        min_length = 1000000
        current_sum = 0

        #sliding window
        for right in range(len(nums)):
            current_sum += nums[right]
            while current_sum >= target:
                min_length = min(min_length, right - left + 1)
                current_sum -= nums[left]
                left += 1
        return min_length if min_length != 1000000 else 0