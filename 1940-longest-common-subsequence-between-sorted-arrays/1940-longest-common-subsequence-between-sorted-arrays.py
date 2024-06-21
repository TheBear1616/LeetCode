class Solution:
    def longestCommonSubsequence(self, arrays: List[List[int]]) -> List[int]:
        result = arrays[0]

        def LCS(tempArray, currArray):
            i = 0
            j = 0
            result = []

            while i < len(tempArray) and j < len(currArray):
                if tempArray[i] == currArray[j]:
                    result.append(tempArray[i])
                    i += 1
                    j += 1
                elif tempArray[i] < currArray[j]:
                    i += 1
                else:
                    j += 1

            return result
        
        for i in range(1, len(arrays)):
            result = LCS(result, arrays[i])

        return result