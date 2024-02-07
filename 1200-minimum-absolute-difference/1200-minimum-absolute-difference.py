class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        result = []
        minDiff = 1e9

        for i in range(1, len(arr)):
            if arr[i] - arr[i-1] < minDiff:
                result = [[arr[i-1], arr[i]]]
                minDiff = arr[i] - arr[i-1]
            elif arr[i] - arr[i-1] == minDiff:
                result.append([arr[i-1], arr[i]])

        return result