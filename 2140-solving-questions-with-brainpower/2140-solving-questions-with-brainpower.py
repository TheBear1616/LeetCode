class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        dp = [-1] * len(questions)
        
        def solve(currProb):
            if currProb >= len(questions):
                return 0
            
            if dp[currProb] != -1:
                return dp[currProb]
            
            points, skip = questions[currProb]
            dp[currProb] = max(solve(currProb + 1), points + solve(currProb + skip + 1))

            return dp[currProb]
        
        return solve(0)
            