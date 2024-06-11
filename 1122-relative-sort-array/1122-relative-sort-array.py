class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr1Dict = Counter(arr1)
        result = []

        for num in arr2:
            result.extend([num] * arr1Dict[num])
            del arr1Dict[num]
        
        for key, val in sorted(arr1Dict.items()):
            result.extend([key] * val)
        
        return result 