class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = len(nums) * (len(nums) + 1)
        total = total / 2
        res = total - sum(nums) 
        return int(res)
        
