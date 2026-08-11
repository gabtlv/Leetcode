class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # 2^n 
        # n = 3 the cardinality of the set should be 8
        length = 2**len(nums)
        #print(length)
        res = []
        for i in range(length):
            subset=[]
            for j in range(length):
                if i & (1 << j):
                    subset.append(nums[j])
            res.append(subset)
        return res 