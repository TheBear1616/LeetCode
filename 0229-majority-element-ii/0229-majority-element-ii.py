class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        countOne, countTwo = 0, 0
        candidateOne, candidateTwo = None, None

        for num in nums:
            if candidateOne == num:
                countOne += 1
            elif candidateTwo == num:
                countTwo += 1
            elif countOne == 0:
                candidateOne = num
                countOne += 1
            elif countTwo == 0:
                candidateTwo = num
                countTwo += 1
            else:
                countOne -= 1
                countTwo -= 1
            
        result = []
        for candidate in [candidateOne, candidateTwo]:
            if nums.count(candidate) > len(nums) // 3:
                result.append(candidate)
        
        return result
 