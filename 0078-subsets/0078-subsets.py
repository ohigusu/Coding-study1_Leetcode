class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []
        sort_num = sorted(nums)
        max_num = max(sort_num)+1
        sort_num.append(max_num)
        def fun(visited,idx):
            n = len(visited)
            if visited and visited[-1] == max_num:
                answer.append(visited[:-1])
                return
            else:
                for i in range(idx,len(sort_num)):
                    if sort_num[i] not in visited:
                        visited.append(sort_num[i])
                        fun(visited,i+1)
                        visited.pop()
        fun([],0)
        return answer
                