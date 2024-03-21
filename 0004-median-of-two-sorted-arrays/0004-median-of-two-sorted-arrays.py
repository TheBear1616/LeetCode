class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(B) < len(A):
            A, B = B, A 

        low = 0
        high = len(A) - 1

        while True:
            midOne = (low + high) // 2
            midTwo = half - midOne - 2

            Aleft = A[midOne] if midOne > -1 else -1e9
            Aright = A[midOne + 1] if midOne + 1 < len(A) else 1e9
            Bleft = B[midTwo] if midTwo > -1 else -1e9
            Bright = B[midTwo + 1] if midTwo + 1 < len(B) else 1e9

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2: return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                high = midOne - 1
            else:
                low = midOne + 1

