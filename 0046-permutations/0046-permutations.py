class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0: return []
        if len(nums) == 1: return [nums]
        result = []
        #부모노드
        for i in range(len(nums)):
            current = nums[i]
            remaining = nums[:i]+nums[i+1:]
            #모든 자식노드
            for p in self.permute(remaining):
                result.append([current]+p)
        return result
