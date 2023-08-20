class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        if len(nums) == 1:
            return [nums.copy()]
        
        for num in nums:
            n = nums.pop(0)
            permutations = self.permute(nums)

            for permutation in permutations:
                permutation.append(n)
            
            result.extend(permutations)
            nums.append(n)
        
        return result