class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [nums]
        result = []
        for i in range(len(nums)):
            current = nums[i]
            remaining = nums[:i]+nums[i+1:]

            for p in self.permute(remaining):
                result.append([current]+p)
        return result