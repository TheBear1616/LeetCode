class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(permutation, counter):
            if len(permutation) == len(nums):
                result.append(permutation.copy())
                return
            
            for num in counter:
                if counter[num] == 0:
                    continue
                
                permutation.append(num)
                counter[num] -= 1
                backtrack(permutation, counter)
                permutation.pop()
                counter[num] += 1
            
        backtrack([], collections.Counter(nums))
        
        return result
