class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        for curr in range(len(nums) - 1):
            if (curr % 2 == 0 and nums[curr] > nums[curr + 1]) or (curr % 2 == 1 and nums[curr] < nums[curr + 1]):
                nums[curr], nums[curr + 1] = nums[curr + 1], nums[curr]

        return