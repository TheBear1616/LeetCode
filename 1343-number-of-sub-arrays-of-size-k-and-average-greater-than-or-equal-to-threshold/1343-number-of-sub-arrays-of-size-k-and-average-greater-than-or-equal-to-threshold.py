class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        left = 0
        count = 0
        wSum = 0

        for right in range(len(arr)):
            wSum += arr[right]
            if (right - left + 1) == k:
                count += 1 if (wSum // k) >= threshold else 0
                wSum -= arr[left]
                left += 1
        
        return count