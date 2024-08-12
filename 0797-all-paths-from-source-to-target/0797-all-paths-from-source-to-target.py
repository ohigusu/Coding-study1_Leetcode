class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.paths = []

        def dfs(graph,node,traversed_path,n):
            traversed_path.append(node)

            if node == n: paths.append(traversed_path[:])

            for neigh in graph[node]: dfs(graph,neigh,traversed_path,n)

            traversed_path.pop()

        dfs(graph,0,[],len(graph)-1)
        return paths

