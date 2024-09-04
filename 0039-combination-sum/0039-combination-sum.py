class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []

        def dfs(visited,rest,start_idx):
            if sum(visited) == target:
                answer.append(visited[:])
            else:
                for i in range(start_idx,len(candidates)):
                    if rest >= candidates[i]:
                        visited.append(candidates[i])
                        dfs(visited,rest - candidates[i],i)
                        visited.pop()
                    
        dfs([],target,0)
        return answer