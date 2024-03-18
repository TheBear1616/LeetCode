# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader(object):
#	 # Compares the sum of arr[l..r] with the sum of arr[x..y]
#	 # return 1 if sum(arr[l..r]) > sum(arr[x..y])
#	 # return 0 if sum(arr[l..r]) == sum(arr[x..y])
#	 # return -1 if sum(arr[l..r]) < sum(arr[x..y])
#    def compareSub(self, l: int, r: int, x: int, y: int) -> int:
#
#	 # Returns the length of the array
#    def length(self) -> int:
#


class Solution:
    def getIndex(self, reader: 'ArrayReader') -> int:
        low = 0
        high = reader.length() - 1

        while low < high:
            mid = low + (high - low) // 2
            isOdd = (high - low + 1) % 2
            comparison = reader.compareSub(low, mid - isOdd, mid + 1, high)
            if comparison == 0:
                return mid
            elif comparison == 1:
                high = mid - isOdd
            else:
                low = mid + 1
        
        return low
        