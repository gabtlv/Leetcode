class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # result of the list 
        result = []
        # 1 2 3
        # 2 3

        # base case if theres only 1 element
        if len(nums) == 1:
            return [nums.copy()]
        
        for i in range(len(nums)):
            initial = nums.pop(0)
            perms = self.permute(nums)

            for perm in perms:
                perm.append(initial)
            result.extend(perms)
            nums.append(initial)
        
        return result