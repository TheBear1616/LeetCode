class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False 

        increasing = 0
        decreasing = len(arr) - 1

        while increasing + 1 < len(arr) and arr[increasing] < arr[increasing + 1]:
            increasing += 1
        
        while decreasing - 1 > -1 and arr[decreasing] < arr[decreasing - 1]:
            decreasing -= 1
        
        if increasing == 0 or decreasing == len(arr) - 1:
            return False
        
        return increasing == decreasing