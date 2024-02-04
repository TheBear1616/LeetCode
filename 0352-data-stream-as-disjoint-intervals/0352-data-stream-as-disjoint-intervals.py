class SummaryRanges:

    def __init__(self):
       self.numsSet = set() 

    def addNum(self, value: int) -> None:
        self.numsSet.add(value)

    def getIntervals(self) -> List[List[int]]:
        nums = sorted(list(self.numsSet))
        res = []
        i = 0

        while i < len(nums):
            start = nums[i]
            while i + 1 < len(nums) and nums[i + 1] == nums[i] + 1:
                i += 1
            res.append([start, nums[i]])
            i += 1

        return res        


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()