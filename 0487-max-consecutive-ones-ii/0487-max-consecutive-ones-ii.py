class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        start = 0
        maxOnesLength = 0
        binary = {1: 0}
        
        for end in range(len(nums)):
            if nums[end] == 1: binary[1] += 1 
            while (end - start + 1) - binary[1] > 1:
                if nums[start] == 1: binary[1] -= 1
                start += 1
 
            maxOnesLength = max(maxOnesLength, end - start + 1)
        
        return maxOnesLength