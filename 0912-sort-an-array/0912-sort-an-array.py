class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        
        mid = len(nums) // 2
        left = self.sortArray(nums[: mid])
        right = self.sortArray(nums[mid: ])

        return self.mergeSort(left, right)
    
    def mergeSort(self, left, right):
        i, j = 0, 0
        res = []

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
        
        res += left[i:] if j == len(right) else right[j:]
        return res
