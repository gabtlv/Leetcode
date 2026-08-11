class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # divide by 2 because it is a BST
        
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2   
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return left # insert it on the left of the middle