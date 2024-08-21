class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        answer = []
        for i in range(len(graph)-1):
            if graph[i] == []:
                last = i
        def backtracking(graph,node,visted):
            #해결 조건과 일치
            if node == len(graph)-1:
                answer.append([0]+visted[:])
            else:
                for neighbor in graph[node]:
                    #후보군
                    if neighbor not in visted:
                        visted.append(neighbor)
                        backtracking(graph,neighbor,visted)
                        visted.pop()
        backtracking(graph,0,[])
        return answer
                


