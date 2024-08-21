class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        if graph == []: return []
        n = len(graph)
        result = []
        queue = [[graph[0],[0]]]
        while queue:
            p,visited = queue.pop()
            for node in p :
                if node == n-1:
                    result.append(visited+[node])
                else:
                    visited.append(node) #방문 체크
                    for next in graph[node]:
                        queue.append([[next],visited[:]])
                    visited.pop()
        return result
				


