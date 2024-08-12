class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        if graph[0] == []: return []
        
        N,path,result = len(graph),{},[]
        
        for i, g in enumerate(graph):path[i] = g
        
        stack = [[path[0], [0]]]

        while stack:
            p, path_history = stack.pop(0)
            
            for node in p:
                if node == N-1:
                    result.append(path_history + [node])

                else:
                    path_history.append(node)
                    for next_path in path[node]:
                            stack.append([[next_path], path_history[:]])
                    path_history.pop()

        return result

