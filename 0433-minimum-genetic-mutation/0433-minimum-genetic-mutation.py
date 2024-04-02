class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        queue = collections.deque([(startGene, 0)])
        seen = {startGene}

        while queue:
            node = queue.popleft()
            gene, minSteps = node[0], node[1]
            if gene == endGene:
                return minSteps
            
            for char in "ACGT":
                for i in range(len(gene)):
                    neighbor = gene[:i] + char + gene[i+1:]
                    if neighbor not in seen and neighbor in set(bank):
                        queue.append((neighbor, minSteps + 1))
                        seen.add(neighbor)
        
        return -1
