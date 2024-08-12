class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = []
         
        def dfs(graph,node,path,n):
            path.append(node)
            if node == n : result.append(path[:])
            else:
                for neigh in graph[node]:
                    dfs(graph,neigh,path,n)  
            path.pop()
            return result
        return dfs(graph,0,[],len(graph)-1)
