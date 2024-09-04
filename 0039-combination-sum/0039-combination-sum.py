class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        #backtracking 식
        #입력데이터는 다음과 같다.
        # visited: 방문한 원소 저장
        # rest: 나머지 값
        # start_idx: 인덱스
        #출력데이터는 다음과 같다.
        # answer: 다 더했을 때 target의 값과 동일한 조합들의 리스트를 저장한 리스트 
        def dfs(visited,rest,start_idx):
            #visited에 저장된 원소들의 합이 target과 같으면(문제해결 조건) answer에 저장
            if sum(visited) == target:
                answer.append(visited[:])
            #문제해결 조건과 부합하지 않으면
            else:
                #start_index부터 candidates의 길이만큼이 자식노드가 된다. 
                for i in range(start_idx,len(candidates)):
                    #후보로 유망한 노드: 그 전 단계에서의 나머지 값보다 작거나 같은 노드
                    if rest >= candidates[i]:
                        #visited에 저장
                        visited.append(candidates[i])
                        #재귀 
                        dfs(visited,rest - candidates[i],i)
                        #끝나면 pop()
                        visited.pop()
        #함수 실행
        dfs([],target,0)
        return answer
