class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergesort(nums):
            if len(nums) == 1: return
            mid = len(nums)//2
            left = nums[:mid]
            right = nums[mid:]
            
            mergesort(left)
            mergesort(right)
            
            mergeTwoSortedArrays(left, right, nums)
        
        def mergeTwoSortedArrays(a, b , nums):
            i, j, k = 0, 0, 0
            while i < len(a) and j < len(b):
                if a[i] < b[j]:
                    nums[k] = a[i]
                    i+=1
                else:
                    nums[k] = b[j]
                    j+=1
                k+=1
            
            nums[k:] = a[i:] if i<len(a) else b[j:]
        
        mergesort(nums)
        return nums