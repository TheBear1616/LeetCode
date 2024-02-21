class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n: return True
        graphMap = { i: [] for i in range(n)}
        for n1, n2 in edges:
            graphMap[n1].append(n2)
            graphMap[n2].append(n1)

        visited = set()
        def dfs(node, prev):
            if node in visited:
                return False
            
            visited.add(node)
            for child in graphMap[node]:
                if child == prev: continue
                if not dfs(child, node): return False
            
            return True
        
        return dfs(0, -1) and len(visited) == n
    