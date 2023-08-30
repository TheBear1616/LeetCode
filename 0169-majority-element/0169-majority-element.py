class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majorEle = nums[0]
        count = 1
        
        for i in range(1, len(nums)):
            count += 1 if majorEle == nums[i] else -1
            if count == 0:
                majorEle = nums[i]
                count = 1
        
        return majorEle