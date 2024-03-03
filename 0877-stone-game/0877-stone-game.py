class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        dp = {}
        totalSum = sum(piles)

        def dfs(i, j):
            if i > j: return 0
            
            if (i, j) in dp: return dp[(i, j)]

            aliceTurn = True if (j - i) % 2 else False
            leftVal = piles[i] if aliceTurn else 0
            rightVal = piles[j] if aliceTurn else 0

            dp[(i, j)] = max(leftVal + dfs(i + 1, j), rightVal + dfs(i, j - 1))

            return dp[(i, j)]
            
        aliceStones = dfs(0, len(piles) - 1)
        
        return True if aliceStones > (totalSum - aliceStones) else False
