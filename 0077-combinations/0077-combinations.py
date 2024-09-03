class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combi,answer = [],[]
        
        for i in range(1,n+1):
            combi.append(i)

        def dfs(visited,idx):
            if len(visited) == k:
                answer.append(visited[:]) #visited로 하면 [[],[[],[]]로 나온다.
            else:
                for i in combi[idx:]:
                    if i not in visited:
                        visited.append(i)
                        next_idx = combi.index(i) + 1
                        dfs(visited,next_idx)
                        visited.pop()
                    
        dfs([],0)
        return answer
