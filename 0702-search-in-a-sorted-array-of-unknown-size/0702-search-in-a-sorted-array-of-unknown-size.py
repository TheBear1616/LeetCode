# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        low = 0
        high = pow(10, 4) - 1

        while low <= high:
            mid = low + (high - low) // 2
            num = reader.get(mid)
            if num == target:
                return mid
            elif num > target:
                high = mid - 1
            else:
                low = mid + 1
        
        return -1