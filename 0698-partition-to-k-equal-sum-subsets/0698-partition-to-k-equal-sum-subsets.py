class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total_sum = sum(nums)
        
        #만약 전체 합이 k로 나누어떨어지지 않으면 불가능
        if total_sum % k != 0:
            return False

        target_sum = total_sum // k  #각 부분집합의 목표 합
        nums.sort(reverse=True)  #큰 숫자부터 처리하면 백트래킹이 더 빨라진다.
        
        #목표 합보다 큰 숫자가 있으면 바로 불가능
        if nums[0] > target_sum:
            return False
        
        visited = [False] * len(nums)  #숫자가 사용됐는지 추적하는 리스트
        
        #백트래킹 함수
        def backtrack(start, current_sum, count):
            
            #만약 k-1개의 부분집합을 만들었다면, 나머지 하나도 완성된 것
            #total_sum = 20, target_sum = 5일 때, 최종 부분집합의 개수는 4개이다. 
            #즉, 3개의 부분집합이 이미 완성되었으면 나머지도 자동으로 완성된다.
            if count == k - 1:
                return True
            
            #현재 부분집합이 목표 합에 도달하면 새로운 부분집합을 시작
            if current_sum == target_sum:
                return backtrack(0, 0, count + 1)
            
            #숫자들을 하나씩 확인하며 상자에 넣기
            for i in range(start, len(nums)):
                
                if not visited[i] and current_sum + nums[i] <= target_sum:
                    visited[i] = True #숫자를 사용한다고 표시
                    if backtrack(i + 1, current_sum + nums[i], count):
                        return True
                    visited[i] = False #실패하면 다시 되돌리기
                    if current_sum + nums[i] == target_sum:
                        break
            return False
        
        #첫 번째 부분집합부터 만들기 시작
        return backtrack(0, 0, 0)
