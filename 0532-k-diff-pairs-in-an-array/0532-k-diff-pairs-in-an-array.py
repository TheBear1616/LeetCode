class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        uniquePairs = set()
        seen = collections.defaultdict(int)

        for num in nums:
            if num - k in seen:
                uniquePairs.add((num - k, num))
            if num + k in seen:
                uniquePairs.add((num, num + k))
            
            seen[num] += 1
        
        return len(uniquePairs)
        