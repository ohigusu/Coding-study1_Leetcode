#sol1
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0: return []
        if len(nums) == 1: return [nums]
        result = []
        for i in range(len(nums)):
            current = nums[i]
            remaining = nums[:i]+nums[i+1:]

            for p in self.permute(remaining):
                result.append([current]+p)
        return result
#sol2
class Solution:
    def permute(self,nums:List[int])->List[List[int]]:
        answer = []
        def backtracking(visited):
            #해결 조건과 일치하면 answer에 저장
            if len(visted) == len(nums) : 
                answer.append(visted[:])
                return
            #해결 조건과 일치하지 않으면
            else:
                #모든 자식 노드에 대해
                for i in range(len(nums)):
                    #후보군
                    if nums[i] not in visted:
                        visted.append(nums[i]) #방문 체크
                        dfs(visted) #백트래킹: 끝까지 파고들어간다.
                        visted.pop() #같은 레벨에 있는 다른 노드들도 확인하기 위해 pop()
                        
                        
            
