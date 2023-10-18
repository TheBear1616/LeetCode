class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        result = 0
        numOfSubarrays = 0
        
        for num in nums:
            if num == 0:
                numOfSubarrays += 1
            else:
                numOfSubarrays = 0
            
            result += numOfSubarrays
        
        return result