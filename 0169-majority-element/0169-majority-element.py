class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majorEle = None
        count = 0

        for num in nums:
            if count == 0: majorEle = num
            count += 1 if num == majorEle else -1
            
        return majorEle