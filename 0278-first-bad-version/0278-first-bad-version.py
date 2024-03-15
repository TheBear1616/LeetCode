# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low, high = 1, n
        while low <= high:
            mid = (low+high)//2
            badVersion = isBadVersion(mid)
            if badVersion and isBadVersion(mid-1) == False:
                return mid
            elif badVersion == False and isBadVersion(mid+1) == True:
                return mid+1
            elif badVersion == False:
                low = mid+1
            else:
                high = mid-1