class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        if graph[0] == []: return []
        
        N,path,result = len(graph),{},[]
        
        for i, g in enumerate(graph):path[i] = g
        
        stack = [[path[0], [0]]]

        while stack:
            p, path_history = stack.pop()
            for each_path in p:
                if each_path == N-1:
                    result.append(path_history + [each_path])

                else:
                    path_history.append(each_path)
                    for next_path in path[each_path]:
                            stack.append([[next_path], path_history[:]])
                    path_history.pop()

        return result

