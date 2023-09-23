class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums2 = nums2
        self.cn1 = collections.Counter(nums1)
        self.cn2 = collections.Counter(nums2)

    def add(self, index: int, val: int) -> None:
        self.cn2[self.nums2[index]] -= 1

        if self.cn2[self.nums2[index]] == 0:
            del self.cn2[self.nums2[index]]

        self.nums2[index] += val
        self.cn2[self.nums2[index]] += 1

    def count(self, tot: int) -> int:
        smaller, larger = (self.cn1, self.cn2) if len(self.cn1) <= len(self.cn2) else (self.cn2, self.cn1)

        return sum(freq*larger[tot-val] for val, freq in smaller.items())

        


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)