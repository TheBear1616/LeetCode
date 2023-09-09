class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = {num: -1 for num in nums2}
        stack = []

        for i in range(len(nums2) - 1):
            if nums2[i] < nums2[i+1]:
                result[nums2[i]] = nums2[i+1]
                while stack and stack[-1] < nums2[i+1]:
                    result[stack.pop()] = nums2[i+1]
            else:
                stack.append(nums2[i])


        return [result[num] for num in nums1]