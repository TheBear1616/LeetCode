class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        left = 0
        right = len(warehouse) - 1
        count = 0
        boxes.sort(reverse = True)
        i = 0

        while left <= right and i < len(boxes):
            if boxes[i] <= warehouse[left]:
                left += 1
                count += 1
            elif boxes[i] <= warehouse[right]:
                right -= 1
                count += 1
            i += 1

        return count
