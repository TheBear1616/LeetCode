class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        cityA = len(costs) // 2
        cityB = len(costs) // 2
        result = 0

        costs.sort(key=lambda x: abs(x[1] - x[0]))

        i = len(costs) - 1

        while i >= 0 and cityA > 0 and cityB > 0:
            if costs[i][0] < costs[i][1]:
                result += costs[i][0]
                cityA -= 1
            else:
                result += costs[i][1]
                cityB -= 1
            
            i -= 1

        while i >= 0 and cityA > 0:
            result += costs[i][0]
            cityA -= 1
            i -= 1
        
        while i >= 0 and cityB > 0:
            result += costs[i][1]
            cityA -= 1
            i -= 1
        
        return result