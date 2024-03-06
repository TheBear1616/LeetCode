class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = {i: [] for i in range(n)}

        for node, child in edges:
            graph[node].append(child)
            graph[child].append(node)
        
        def dfs(node, par):
            time = 0

            for child in graph[node]:
                if child == par:
                    continue

                childTime = dfs(child, node)
                if childTime or hasApple[child]:
                    time += 2 + childTime
            
            return time
        
        return dfs(0, -1)
