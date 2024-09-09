class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []
        def backtrack(visited,idx):
            answer.append(visited[:])
            for i in range(idx,len(nums)):
                if nums[i] not in visited:
                    visited.append(nums[i])
                    backtrack(visited,i+1)
                    visited.pop()
        backtrack([],0)
        return answer
