class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        majorEle = -1

        for i in range(len(arr)-1, -1, -1):
            currEle = arr[i]
            arr[i] = majorEle
            majorEle = max(majorEle, currEle)
        
        return arr