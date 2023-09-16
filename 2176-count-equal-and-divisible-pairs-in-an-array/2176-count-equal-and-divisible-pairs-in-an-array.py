class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        idxDict = defaultdict(list)
        count = 0

        for idx, num in enumerate(nums):
            if num in idxDict:
                for index in idxDict[num]:
                    if (index * idx) % k == 0:
                        count += 1
            idxDict[num].append(idx)
        
        return count