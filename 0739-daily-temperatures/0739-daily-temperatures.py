class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        
        for i in range(len(temperatures) - 1):
            if temperatures[i] < temperatures[i+1]:
                result[i] = 1
                while stack and temperatures[i+1] > stack[-1][0]:
                    value, index = stack.pop()
                    result[index] = (i+1) - index
            else:
                stack.append((temperatures[i], i))
        
        return result
