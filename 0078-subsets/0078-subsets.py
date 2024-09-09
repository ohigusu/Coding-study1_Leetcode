class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []
        def fun(visited,idx):
            answer.append(visited[:])
            for i in range(idx,len(sort_num)):
                if sort_num[i] not in visited:
                    visited.append(sort_num[i])
                    fun(visited,i+1)
                    visited.pop()
        fun([],0)
        return answer
                