class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        if graph[0] == []:
            return []
        
        N = len(graph)
        path = {}
        for i, g in enumerate(graph):
            path[i] = g
        
        stack = [[path[0], [0]]]
        ret_path = []
        while stack:
            # print 'stack =',stack
            p, path_history = stack.pop()
            for each_path in p:
                if each_path == N-1:
                    ret_path.append(path_history + [each_path])
                    continue
                if each_path not in path_history:
                    path_history.append(each_path)
                    for next_path in path[each_path]:
                        if next_path not in path_history:
                            stack.append([[next_path], path_history[:]])
                    path_history.pop()
        return ret_path

