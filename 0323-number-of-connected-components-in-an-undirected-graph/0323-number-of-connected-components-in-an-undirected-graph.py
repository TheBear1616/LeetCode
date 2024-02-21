class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if not n: return True
        graphMap = {i:[] for i in range(n)}
        for node, child in edges:
            graphMap[node].append(child)
            graphMap[child].append(node)
        
        visited = set()

        def dfs(node, prev):
            if node in visited:
                return
            
            visited.add(node)
            for child in graphMap[node]:
                if child == prev: continue
                dfs(child, node)
            
            return
        
        result = 0
        for i in range(n):
            if i not in visited:
                dfs(i, -1)
                result += 1
        
        return result