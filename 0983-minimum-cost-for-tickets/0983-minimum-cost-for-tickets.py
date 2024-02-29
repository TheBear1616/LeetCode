class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        lastDay = days[-1]
        dp = [-1] * (lastDay + 1)
        isTravelNeeded = set(days)

        def solve(currDay):
            if currDay > lastDay:
                return 0
            
            if currDay not in isTravelNeeded:
                return solve(currDay + 1)
            
            if dp[currDay] != -1:
                return dp[currDay]
            
            oneDay = costs[0] + solve(currDay + 1)
            sevenDay = costs[1] + solve(currDay + 7)
            thirtyDay = costs[2] + solve(currDay + 30)

            dp[currDay] = min(oneDay, sevenDay, thirtyDay)

            return dp[currDay]
        
        return solve(days[0])
